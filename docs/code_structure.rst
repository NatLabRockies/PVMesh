Code Structure
==============

Main modules
------------

* ``pvmesh/mesh_generator.py``: Core geometry and mesh creation workflow.
* ``pvmesh/guipytk.py``: GUI for editing parameters, generating input sets,
  and launching mesh runs.


Mesh generator workflow
-----------------------

At a high level, ``mesh_generator.py``:

1. Loads input variables from file.
2. Computes geometric dimensions for layers, frame, and mounting zones.
3. Builds CAD entities in Gmsh and synchronizes geometry.
4. Tags surfaces/volumes with domain markers.
5. Exports mesh files in the selected format.

Geometry is assembled from layered panel components and frame-related features,
then finalized with seal-region construction to close the frame-to-laminate
gap before meshing.

The meshing pipeline assigns 1D/2D/3D entities and applies adaptive refinement
to reduce element density in low-gradient regions.


GUI workflow
------------

The GUI in ``guipytk.py``:

1. Loads defaults from ``original.txt``.
2. Lets users edit variables and validation highlights numeric fields.
3. Expands comma-separated values into parameter combinations.
4. Writes case directories (for example ``input1``, ``input2``).
5. Executes ``mesh_generator.py`` case by case.

For each case, the directory includes generated input text, geometry
intermediates (including ``.brep``), and solver-ready mesh output.

Testing
-------

The unit test mirrors mesh generation behavior and validates key path logic.
For CI and local checks, run:

.. code-block:: bash

   pytest pvmesh/tests

Interoperability notes
----------------------

The code is designed to support mesh export and import workflows used with
COMSOL, ANSYS, ABAQUS, and FEniCS/FEniCSx via the supported output formats.
