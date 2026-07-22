Input Reference
===============

PVMesh reads key-value pairs from text input files (for example ``original.txt``
or generated ``input_*.txt`` files).

Units
-----

Input geometry and meshing parameters are expected in millimeters.

Geometry variables
------------------

* ``cell_thick``: Cell thickness
* ``cell_width``: Cell width
* ``cell_length``: Cell length
* ``n_cell_length``: Number of cells along x
* ``n_cell_width``: Number of cells along y
* ``cell_cell_gap_x``: Gap between cells along x
* ``cell_cell_gap_y``: Gap between cells along y
* ``perimeter_margin``: Margin around the cell matrix

Layer thickness variables
-------------------------

* ``front_glass_thick``
* ``front_encap_thick``
* ``back_encap_thick``
* ``back_sheet_thick``

Frame and seal variables
------------------------

* ``clip_thick``
* ``seal_length``
* ``frame_thick``
* ``a``, ``b``, ``c``, ``h`` (frame geometry controls)

Meshing and mounting variables
------------------------------

* ``mesh_size_in_cell``
* ``mesh_size_out_cell``
* ``mounting_area_shape`` (for example ``square`` or ``circle``)
* ``mounting_area_size``
* ``mounting_location``: normalized location parameter used to place mounting
   zones along panel edges

Typical defaults used in manuscript examples are ``mesh_size_in_cell = 12`` and
``mesh_size_out_cell = 3``.

Output variable
---------------

* ``file_format``: Output mesh format extension

Input format example
--------------------

.. code-block:: text

   cell_thick: 0.17
   cell_width: 182.0
   cell_length: 182.0
   n_cell_length: 12
   n_cell_width: 6
   file_format: .msh

Useful derived relationships
----------------------------

For parameter sweeps with list-valued inputs, total generated meshes are:

.. math::

   N_{\text{meshes}} = \prod_{i=1}^{k} n_i

where ``n_i`` is the number of values assigned to parameter ``i``.

Mounting location follows the normalized relation:

.. math::

   \eta = \frac{l_0}{l}

where ``l`` is panel length and ``l_0`` is the edge-to-mount-center distance.
