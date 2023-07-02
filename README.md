# Simulating a spinodal decomposition process governed by Cahn-Hilliard equation

This repository contains the material produced for the exam "Software and Computing for Applied Physics" - University of Bologna. It consists of a simulation of a spinodal decomposition process, whose dynamics is described by the Cahn-Hilliard equation.

## Spinodal decomposition and Cahn-Hilliard equation

Spinodal decomposition is a mechanism by which a mixture of two liquid or solid components can rapidly unmix from a single thermodynamic phase into two coexisting phases, each with its own chemical composition and physical properties. An example could be an hot mixture of water and an oil. At high temperatures the oil and the water may mix to form a single thermodynamic phase in which water molecules are surrounded by oil molecules and vice verse. The mixture is then suddenly cooled to a temperature at which thermodynamic equilibrium favors an oil-rich phase coexisting with a water-rich phase. Spinodal decomposition then occurs when the oil and water molecules immediately start to cluster together into microscopic water-rich and oil-rich clusters throughout the liquid. These clusters then rapidly grow and coalesce until there is a single macroscopic oil-rich cluster, the oil-rich phase, and a single water-rich cluster, the water-rich phase.

Spinodal decomposition is a continuous phase transition, whose order parameter is the concentration $c$ of one of the two mixture components. The transition arises from small perturbations of the equilibrium concentration of the mixture, and is driven by a diffusion process of the mixture components.
Given a mixture of two components A and B, with concentrations respectively $(1-c(\vec r))$ and $c(\vec r)$, the diffusion process of species B is described by the following diffusion equation:
$$\vec J_B = -M\vec \nabla $$


## Phase-field modelling of microstructures

## Structure of the project

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
