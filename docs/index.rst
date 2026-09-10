PVmesh Documentation
====================

PVmesh is an open-source Python tool for generating high-fidelity,
adaptive finite-element meshes for photovoltaic modules.
It supports multilayer panel geometries, frame details, and mounting zones
that are often difficult to mesh robustly with generic workflows.

Built on Gmsh, PVmesh automates geometry construction, partitioning,
domain/boundary tagging, and export for downstream finite-element solvers.

Supported output formats include:

* ``.msh`` for ANSYS
* ``.bdf`` for COMSOL
* ``.vtk`` for FEniCS/FEniCSx
* ``.inp`` for ABAQUS

Highlights
----------

* PVmesh automates high-fidelity finite-element mesh generation for PV modules.
* Flexible mesh controls improve element quality in multilayer structures.
* Input-list workflows support automated parametric modeling.
* Multiple mesh export formats support common FE solver pipelines.
* A GUI supports non-programmatic setup and batch generation.


.. toctree::
   :maxdepth: 2
   :caption: Contents

   installation
   usage
   input_reference
   code_structure
   softwarex_alignment
   reference


