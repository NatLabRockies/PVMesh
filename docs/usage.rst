How to use PVMesh
=====

PVMesh can be used in two modes:

* Graphical interface (GUI)
* Script-driven mesh generation

Run the GUI
-----------

From the project root:

.. code-block:: bash

   python pvmesh/guipytk.py

The GUI loads defaults from ``original.txt`` and can generate one or more input
files for parametric studies.

Run from input files
--------------------

The mesh generator script can run on input files produced by the GUI.
The explicit CLI invocation is:

.. code-block:: bash

   python pvmesh/mesh_generator.py <input_file> <output_folder>

If no CLI arguments are provided, the script uses the default input path
``input1/input_1.txt``. If that file is missing, input parsing falls back to
``original.txt``.


