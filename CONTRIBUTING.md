# Contributing to PVmesh

Thank you for your interest in contributing to PVmesh.
Contributions of all kinds are welcome, including:

- Bug reports and reproducible issue cases.
- New features and mesh-generation improvements.
- Test improvements.
- Documentation updates.

## Before You Start

1. Check whether your topic already exists in the issue tracker: https://github.com/NREL/PVmesh/issues
2. If not, open a new issue with a clear description and expected behavior.
3. Comment on the issue before starting implementation work, especially for larger changes.

## Development Setup

Use the project conda environment from the repository root:

```bash
mamba env create -n pvmesh -f environment.yaml
mamba activate pvmesh
```

This environment includes runtime dependencies plus testing and documentation tooling.

## Repository Layout

- `pvmesh/mesh_generator.py`: script-driven geometry and mesh generation.
- `pvmesh/guipytk.py`: GUI workflow and case generation.
- `pvmesh/tests/`: pytest suite.
- `docs/`: Sphinx documentation source.
- `original.txt`: default input parameters used by the GUI and fallback behavior.

## Local Validation

Run tests before opening a pull request:

```bash
pytest -sv pvmesh/tests/
```

Format code with Black:

```bash
black pvmesh
```

Build docs locally when changing documentation:

```bash
cd docs
make html
```

## Coding Guidelines

- Follow PEP 8 and keep code changes focused.
- Prefer small, reviewable pull requests over large mixed changes.
- Add or update tests when fixing bugs or adding behavior.
- Keep user-facing defaults and input-file behavior backward compatible where practical.

## Pull Request Checklist

Before submitting a pull request, confirm:

- The change is linked to an issue (or clearly justified).
- `pytest -sv pvmesh/tests/` passes locally.
- `black pvmesh` has been applied.
- Documentation is updated when behavior, inputs, or outputs changed.
- The PR description explains what changed, why it changed, and how it was validated.

## CI Notes

Current CI runs:

- Pytest on Ubuntu and macOS.
- Black formatting checks.

If your change affects platform behavior, please call that out in the PR description.

## Reporting Bugs

When reporting a bug, include:

- PVmesh version or commit hash.
- Operating system and Python version.
- Input file (or minimal subset) to reproduce.
- Full traceback and a short reproduction sequence.

Thanks for helping improve PVmesh.
