---
title: 'PVMesh: A Tool to Create High-Fidelity and Adaptive Finite Element Mesh for PV Systems.'
tags:
  - Python
  - PV
  - Mesh
  - GMSH
  - PVMesh
authors:
  - name: Walid Arsalane
    orcid: 0009-0006-0935-0690
    equal-contrib: true
    affiliation: 1 
  - name: Munjal Purnkant Shah
    orcid: 0000-0002-6120-6016
    equal-contrib: true
    affiliation: 1
  - name: Xin He
    orcid: 0000-0002-3457-2547
    equal-contrib: true
    affiliation: 1 
affiliations:
 - name: National Laboratory of the Rockies, United States
   index: 1
date: 17 July 2026
bibliography: sample.bib

# # Optional fields if submitting to a AAS journal too, see this blog post:
# # https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
# aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
# aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

PVMesh is an open-source Python package for generating high-fidelity, adaptive finite-element meshes for photovoltaic (PV) modules. It is designed for multilayer PV geometries that are difficult to mesh robustly because of thin layers, varying thickness scales, and frame details. Built on Gmsh [@geuzaine2009gmsh], PVMesh automates geometry construction, partitioning, and mesh export to common solver formats (`.msh`, `.vtk`, `.inp`, `.bdf`).

The tool supports parameter lists and generates one mesh per parameter combination, enabling efficient parametric studies over panel layout and mesh settings in a single run. A graphical user interface (GUI) is provided to simplify model setup for users who do not want to write code directly.

The implementation discussed in this paper is available in the public repository [@pvmesh_repo].



# Statement of need

Finite-element (FE) modeling is widely used to analyze PV reliability and durability, including failure mechanisms such as crack initiation and propagation in cells, glass, and encapsulation layers. In this context, mesh quality strongly affects simulation accuracy and solver convergence. Achieving durability targets for PV systems has been framed as an important research challenge by the Durable Module Materials consortium (DuraMAT) [@duramat].

Existing workflows are often time-consuming for PV modules because: (1) module geometry is multilayered and thin, (2) different regions require different mesh resolutions, (3) commercial solvers rely on different mesh formats, and (4) geometry/mesh parametric sweeps are not always straightforward in GUI-first tools. Commercial FE ecosystems also differ in mesh import formats and sweep tooling, including ABAQUS [@manual2012abaqus], COMSOL [@manualcomsol62], and ANSYS [@manualansys2024]. PVMesh addresses these gaps by providing a PV-specific meshing workflow that is automated, flexible, and interoperable across major FE ecosystems.



# State of the field                                                                                                                  

PV FE studies commonly simplify module structure to reduce setup complexity, but these simplifications can reduce physical fidelity. Examples include spring-mass abstractions for panel aeroelastic response [@young2020fluid] and single-cell FE studies for thermal stress and delamination [@he2018finite; @bosco2020viscoelastic]. More detailed structural representations can materially affect analysis quality [@hartley2023analyzing].

General-purpose meshing tools are powerful but not specialized for PV module conventions (cell arrays, layer partitioning, mounting regions, and solver-ready tagging). The multilayer panel structure and frame geometry that motivate this specialization are illustrated in the source material using prior PV structural references [@he2018finite; @deceglie2023whatscracking]. PVMesh contributes a domain-focused layer on top of Gmsh [@geuzaine2009gmsh] by combining:

- PV-specific geometry parameterization.
- Layer partitioning aligned to cell layout for improved mesh control.
- Built-in support for multiple output formats used by COMSOL, ANSYS, and FEniCSx.
- Batch generation for parametric studies.

This combination reduces setup overhead while preserving high-fidelity model construction.



# Software design

PVMesh is implemented in Python and uses Gmsh [@geuzaine2009gmsh] for geometry and mesh generation. Its workflow is:

1. Read geometry and meshing parameters from GUI-generated inputs.
2. Construct multilayer PV geometry including frame, seal, mounting, glass, encapsulants, cells, and backsheet.
3. Partition layers to align with cell topology and improve mesh-size transitions.
4. Assign physical groups (domains and boundaries) to support downstream material and boundary-condition mapping.
5. Generate meshes and export to multiple FE formats.

The GUI exposes geometry and meshing parameters, including mounting area shape/size/location and separate mesh controls for cell-domain regions versus other domains. This enables targeted refinement while limiting total degrees of freedom.

To improve interoperability, exported meshes were validated in COMSOL, ANSYS, and FEniCSx. The project also includes ANSYS-oriented handling to preserve useful surface partitioning behavior during import, while mesh export targets the formats discussed for COMSOL, ANSYS, and ABAQUS compatibility [@manualcomsol62; @manualansys2024; @manual2012abaqus].



# Research impact statement

PVMesh lowers the barrier to creating high-quality PV FE meshes for reliability and structural studies. By automating repetitive setup steps and enabling batch mesh generation, it makes large parametric campaigns more practical.

In verification workflows across COMSOL, ANSYS, and FEniCSx, meshes generated by PVMesh were successfully imported and used in representative elasticity simulations with consistent stress-field behavior. This cross-platform usability supports reproducible modeling pipelines and faster method transfer between research groups that use different solvers. The software artifact associated with this paper is the public repository [@pvmesh_repo].



# Mathematics

PVMesh uses simple but important geometric and combinatorial relationships in its setup.

Given list-valued parameter inputs, the number of generated meshes is the Cartesian-product size:

$$
N_{\text{meshes}} = \prod_{i=1}^{k} n_i
$$

where $n_i$ is the number of candidate values for parameter $i$.

For mounting-position specification, the location parameter is normalized by panel length:

$$
\eta = \frac{l_0}{l}
$$

where $l$ is panel length and $l_0$ is the distance from the mounting-area center to the nearest panel edge.

For COMSOL domain indexing (as documented in the source manuscript), a model with

$$
n = n_{\text{cell,width}} \times n_{\text{cell,length}}
$$

cells contains

$$
N_{\text{domains}} = (n+2)\times 5 + 9
$$

domains in the imported geometry bookkeeping.



# Citations

- `@duramat` -> "DuraMAT. https://www.duramat.org/about."
- `@young2020fluid` -> "Young, Ethan, Xin He, Ryan King, and David Corbus. A fluid-structure interaction solver for investigating torsional galloping in solar-tracking photovoltaic panel arrays. Journal of Renewable and Sustainable Energy 12(6), 2020."
- `@he2018finite` -> "He, Xin, and Nicholas S. Bosco. Finite element simulation of mixed-mode PV encapsulant delamination based on cohesive zone model. National Renewable Energy Lab. (NREL), Golden, CO (United States), 2018."
- `@bosco2020viscoelastic` -> "Bosco, Nick, Martin Springer, and Xin He. Viscoelastic material characterization and modeling of photovoltaic module packaging materials for direct finite-element method input. IEEE Journal of Photovoltaics 10(5): 1424-1440, 2020."
- `@hartley2023analyzing` -> "Hartley, James Y., and Tariq Khraishi. Analyzing photovoltaic module mechanics using composite plate theories and finite element solutions. Journal of Composite Materials 57(22): 3573-3583, 2023."
- `@manual2012abaqus` -> "Manual, Abaqus Scripting User's. Abaqus 6.11. http://130.149 89(2080): v6, 2012."
- `@manualcomsol62` -> "Reference Manual. COMSOL 6.2. Comsol, Inc., 2023."
- `@manualansys2024` -> "User Manual. ANSYS 2024R1. ANSYS, Inc., 2023."
- `@deceglie2023whatscracking` -> "Deceglie, Michael, Nicholas Bosco, Timothy Silverman, and Martin Springer. WhatsCracking [SWR-23-03]. National Renewable Energy Laboratory (NREL), Golden, CO (United States), 2023."
- `@geuzaine2009gmsh` -> "Geuzaine, Christophe, and Jean-Francois Remacle. Gmsh: A 3-D finite element mesh generator with built-in pre- and post-processing facilities. International Journal for Numerical Methods in Engineering 79(11): 1309-1331, 2009."
- `@pvmesh_repo` -> "National Laboratory of the Rockies. PVMesh Repository, 2026. Source code and documentation for PVMesh."

<!-- # Figures

![Figure 1a: Multilayered structure of PV panel [@he2018finite].](figures/figure1a.png)

![Figure 1b: Complex geometry of the frame cross section [@deceglie2023whatscracking].](figures/figure1b.png)

![Figure 2: Graphic user interface (GUI) of the PVMesh.](figures/figure2.png)

![Figure 3: Geometry after Partition.](figures/figure3.png)

![Figure 4: Generated mesh in a panel consists of 12 by 6 cells (opened in GMSH).](figures/figure4.png)

![Figure 5: Mesh import window setting in COMSOL.](figures/figure5.png)

![Figure 6: Imported Mesh of a Full Panel with 72 Cells in COMSOL.](figures/figure6.png)

Table 1 in the LaTeX source: Markers of Domains in COMSOL.

![Figure 7: Simulated von-mises stress field from COMSOL.](figures/figure7.png)

![Figure 8: Checking "thickness" box when loading .inp file to ANSYS Mechanical.](figures/figure8.png)

![Figure 9: Imported mesh of a full panel with 72 cells in ANSYS.](figures/figure9.png)

![Figure 10: Selection of surfaces for assignment of boundary conditions.](figures/figure10.png)

![Figure 11: Simulated von-mises stress field from ANSYS.](figures/figure11.png)

![Figure 12: Simulated von-mises stress field from FEniCSx.](figures/figure12.png) -->

# AI usage disclosure

No generative AI tools were used in the development of this software, the writing
of this manuscript, or the preparation of supporting materials.

# Acknowledgements

This work was authored by the National Laboratory of the Rockies for the U.S. Department of Energy (DOE), operated under Contract No. DE-AC36-08GO28308. This work was supported by the Laboratory Directed Research and Development (LDRD) Program at the National Laboratory of the Rockies. The views expressed in the article do not necessarily represent the views of the DOE or the U.S. Government. The U.S. Government retains and the publisher, by accepting the article for publication, acknowledges that the U.S. Government retains a nonexclusive, paid-up, irrevocable, worldwide license to publish or reproduce the published form of this work, or allow others to do so, for U.S. Government purposes.

# References

References are linked through `sample.bib` in the YAML header.

Paper-to-repository bridge for reproducibility:

- Public source repository for the software described in this paper: [@pvmesh_repo].
- Primary user documentation is linked from the repository `README.md`.
- GUI workflow entry point in the repository is `pvmesh/guipytk.py`.
- CLI mesh generation entry point in the repository is `pvmesh/mesh_generator.py`.
- Default parameter set used by the tool is `original.txt`.
- Environment specification for reproducing dependencies is `environment.yaml`.