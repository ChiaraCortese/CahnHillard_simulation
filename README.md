# Simulating a spinodal decomposition process governed by Cahn-Hilliard equation

This repository contains the material produced for the exam "Software and Computing for Applied Physics" - University of Bologna. It consists of a simulation of a spinodal decomposition process, whose dynamics is described by the Cahn-Hilliard equation.

## Spinodal decomposition and Cahn-Hilliard equation

Spinodal decomposition is a mechanism by which a mixture of two liquid or solid components A and B can rapidly unmix from a single thermodynamic phase into two coexisting phases, one A-rich and one B-rich, each with its own chemical composition and physical properties.

Spinodal decomposition is a continuous phase transition, whose order parameter is the concentration $c$ of one of the two mixture components, a locally-conserved quantity. The transition arises in materials with a miscibility gap, meaning that small, local perturbations of the equilibrium concentration of the homogeneous mixture can cause the system to develop local clusters of A or B components until macroscopic A-rich and B-rich domains are formed. The different domains are separated by *diffusion interfaces*, characterized by the presence of a concentration gradient. 
The transition is driven by a diffusion process of the mixture components that aims to minimize the system's free energy.  Given a mixture of two components A and B, with concentrations respectively $(1-c(\vec r))$ and $c(\vec r)$, when subjected to a local concentration perturbation, the diffusion process of species B is described by the following diffusion equation:
$$\vec J_B = -M\vec \nabla \Phi (\vec r),$$
where $M$ is the average mobility of species B, and $\Phi(\vec r)$ is a generalized diffusion potential that to the diffusive term of the homogeneous mixture case, governed by the chemical potential $\mu$, adds a penalty due to the clustering going against the concentration gradient at the diffuse interface:
$$\Phi (\vec r) = \mu - 2k\nabla^2 c(\vec r) = \frac{\partial f^{hom}}{\partial c} - 2k\nabla^2 c(\vec r),$$
where $k$ is a coefficient depending on the species involved, while $\mu$ was substitued using its relation with the free energy $f^{hom}$ of the homogeneous mixture case.
Since the $c$ is a locally-conserved quantity, the continuity equation also holds:
$$\frac{\partial c}{\partial t} + \vec{\nabla} \cdot \vec{J}_B = 0.$$

By combining the two equations, we obtain the **Cahn-Hilliard equation**:
$$\frac{\partial c}{\partial t} = \vec{\nabla} \cdot \Bigl\lbrace M\vec{\nabla} \Bigl( \frac{\partial f^{hom}}{\partial c} - 2k\nabla^2 c(\vec r)\Bigr)\Bigr\rbrace.$$

This derivation relies on phase-field modeling: with this method, a microstructure with compositional and/or structural domains, and thus interfaces, is described as a whole with a set of field variables. The field variables are assumed to be continuous across the interfacial regions. Common field variables are the local composition and the interface orientation.
In this simulation, only the local composition will be considered as a phase variable.

For more info on Cahn-Hilliard equation and spinodal decomposition, check Balluffi, R.W., Allen, S.M. and Carter, W.C. (2005). Spinodal and Order–Disorder Transformations. In *Kinetics of Materials* (eds R.W. Balluffi, S.M. Allen and W.C. Carter), John Wiley & Sons, Inc. doi: [https://doi.org/10.1002/0471749311.ch18]
For more info on phase-field modeling, check Long-Qing Chen, Phase-Field Models for Microstructure Evolution. *Annual Review of Materials Research* (2002). doi: [https://doi.org/10.1146/annurev.matsci.32.112001.132041]

## Structure of the project

In this project, a 2D microstructure was modeled as a grid of N-by-N subcells of x- and y-dimensions respectively $dx$ and $dy$. Each subcell concentration was initialized from a constant value $c_0$ to whom it was added or subtracted a random fluctuation of maximum amplitude $c_{noise}$.
## How to run the simulation and plot the results

To run the simulation, first modify the simulation.txt file

## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
