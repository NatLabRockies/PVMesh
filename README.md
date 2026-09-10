# PVmesh


PVmesh is an open-source Python tool for generating high-fidelity,
adaptive finite-element meshes for photovoltaic modules.
It supports multilayer panel geometries, frame details, and mounting zones
that are often difficult to mesh robustly with generic workflows.

Built on Gmsh, PVmesh automates geometry construction, partitioning,
domain/boundary tagging, and export for downstream finite-element solvers.

Supported output formats include:
- `.msh` for ANSYS
- `.bdf` for COMSOL
- `.vtk` for FEniCS/FEniCSx
- `.inp` for ABAQUS

For more information, visit the [PVmesh Documentation](https://pvmesh.readthedocs.io/en/latest/index.html).

[![test_pvade](https://github.com/NREL/PVmesh/actions/workflows/test_pvmesh.yaml/badge.svg)](https://github.com/NREL/PVmesh/actions/workflows/test_pvmesh.yaml)
[![Documentation Status](https://readthedocs.org/projects/pvmesh/badge/?version=latest)](https://pvmesh.readthedocs.io/en/latest/?badge=latest)


## Getting Started

PVmesh relies on:

- Python
- Gmsh Python bindings
- PyQt5 for the GUI

Recommended environment setup from the project root:

```
mamba env create -n pvmesh -f environment.yaml
```

The environment can be activated using the command:

```
mamba activate pvmesh
```
## Citation

To cite PVmesh, please use the "Cite this repository" feature available on the right-hand side of this repository page or copy the BibTeX reference below:

```bash
@software{doecode_191518,
    author = {He, Xin and Arsalane, Walid},
    doi = {10.11578/dc.20260901.6},
    month = feb,
    title = {{PVade (PV Aerodynamic Design Engineering) [SWR-23-49]}},
    url = {https://github.com/NatLabRockies/PVMesh/},
    year = {2025}
}
```
