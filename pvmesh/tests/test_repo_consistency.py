import ast
import os
import sys
from pathlib import Path

import pytest


def _load_mesh_generator_functions(*names: str):
    """Load selected functions from mesh_generator.py without executing script body."""
    repo_root = Path(__file__).resolve().parents[2]
    mesh_generator = repo_root / "pvmesh" / "mesh_generator.py"
    source = mesh_generator.read_text(encoding="utf-8")
    module = ast.parse(source)

    selected = []
    for node in module.body:
        if isinstance(node, ast.FunctionDef) and node.name in names:
            selected.append(node)

    isolated = ast.Module(body=selected, type_ignores=[])
    namespace = {"os": os, "sys": sys}
    exec(compile(isolated, str(mesh_generator), "exec"), namespace)
    return namespace


def test_process_input_file_parses_expected_types(tmp_path) -> None:
    namespace = _load_mesh_generator_functions("process_input_file")
    process_input_file = namespace["process_input_file"]

    input_file = tmp_path / "input_case.txt"
    input_file.write_text(
        "\n".join(
            [
                "cell_thick: 0.2",
                "n_cell_length: 2",
                "n_cell_width: 3",
                "front_glass_thick: 3.1",
                "front_encap_thick: 0.4",
                "back_encap_thick: 0.5",
                "file_format: vtk",
                "cell_width: 180.0",
                "cell_length: 181.0",
                "back_sheet_thick: 0.35",
                "perimeter_margin: 10.0",
                "cell_cell_gap_x: 2.5",
                "cell_cell_gap_y: 2.5",
                "clip_thick: 6.0",
                "seal_length: 2.0",
                "frame_thick: 1.5",
                "a: 35.0",
                "b: 4.0",
                "c: 12.0",
                "h: 50.0",
                "mesh_size_in_cell: 12",
                "mesh_size_out_cell: 3",
                "mounting_area_shape: square",
                "mounting_area_size: 10",
                "mounting_location: 0.3",
            ]
        ),
        encoding="utf-8",
    )

    parsed = process_input_file(str(input_file))

    assert len(parsed) == 25
    assert parsed[0] == pytest.approx(0.2)
    assert parsed[1] == 2
    assert parsed[2] == 3
    assert parsed[9] == "vtk"
    assert parsed[22] == "square"
    assert parsed[24] == pytest.approx(0.3)


def test_process_input_file_falls_back_to_original_txt(monkeypatch) -> None:
    namespace = _load_mesh_generator_functions("process_input_file")
    process_input_file = namespace["process_input_file"]

    repo_root = Path(__file__).resolve().parents[2]
    monkeypatch.chdir(repo_root)

    parsed = process_input_file("this_file_does_not_exist.txt")

    assert len(parsed) == 25
    assert parsed[0] == pytest.approx(0.17)
    assert parsed[1] == 3
    assert parsed[2] == 2
    assert parsed[9] == "vtk"


def test_add_to_domain_markers_tracks_index_and_metadata() -> None:
    namespace = _load_mesh_generator_functions("_add_to_domain_markers")
    add_to_domain_markers = namespace["_add_to_domain_markers"]

    namespace["domain_markers"] = {"_current_idx": 1}
    add_to_domain_markers("frm", [10, 11], "cell")
    add_to_domain_markers("sur5", [5], "facet")

    markers = namespace["domain_markers"]
    assert markers["frm"]["idx"] == 1
    assert markers["frm"]["gmsh_tags"] == [10, 11]
    assert markers["frm"]["entity"] == "cell"
    assert markers["sur5"]["idx"] == 2
    assert markers["sur5"]["entity"] == "facet"
    assert markers["_current_idx"] == 3


def test_surface_and_volume_tag_helpers_delegate_to_marker_builder() -> None:
    namespace = _load_mesh_generator_functions("surface_tags", "volume_tags")

    recorded_calls = []

    def fake_add_to_domain_markers(name, tags, entity):
        recorded_calls.append((name, tags, entity))

    namespace["_add_to_domain_markers"] = fake_add_to_domain_markers

    surface_count = namespace["surface_tags"]([(2, 4), (2, 9)], 0)
    volume_count = namespace["volume_tags"](
        [[101], [102], [103]],
        0,
        ["frm", "mounting", "seal"],
        2,
    )

    assert surface_count == 2
    assert volume_count == 2
    assert ("sur4", [4], "facet") in recorded_calls
    assert ("sur9", [9], "facet") in recorded_calls
    assert ("frm", [101], "cell") in recorded_calls
    assert ("mounting", [102], "cell") in recorded_calls
