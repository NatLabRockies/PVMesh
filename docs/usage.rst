How to use PVmesh
=====

PVmesh can be used in two modes:

* Graphical interface (GUI)
* Script-driven mesh generation

Run the GUI
-----------

From the project root:

.. code-block:: bash

   python pvmesh/guipytk.py

The GUI loads defaults from ``original.txt`` and can generate one or more input
files for parametric studies.

During execution, the GUI writes input files and launches ``mesh_generator.py``
for each generated case.

Mesh outputs are written using the base name ``panel_geo`` with the extension
selected by ``file_format`` (for example ``.msh``, ``.bdf``, ``.vtk``, ``.inp``).

The GUI view illustrates how geometry and frame
parameters are controlled through editable fields.

Run from input files
--------------------

The mesh generator script can run on input files produced by the GUI.
The explicit CLI invocation is:

.. code-block:: bash

   python pvmesh/mesh_generator.py <input_file> <output_folder>

If no CLI arguments are provided, the script uses the default input path
``input1/input_1.txt``. If that file is missing, input parsing falls back to
``original.txt``.

Legacy single-file workflows that use ``input.txt`` are also supported as long
as the file follows the same key-value structure as ``original.txt``.

For a quick default run, this command is still valid:

.. code-block:: bash

   python pvmesh/mesh_generator.py


Parametric studies
------------------

PVmesh supports comma-separated values for one or more input variables.
The tool expands all parameter combinations, generates one input file per case,
and meshes each case.

Each case directory contains the generated input file, the ``.brep`` geometry,
and the exported mesh.


