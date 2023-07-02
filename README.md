# Simulating a spinodal decomposition process governed by Cahn-Hilliard equation

This repository contains the material produced for the exam "Software and Computing for Applied Physics" - University of Bologna. It consists of a simulation of a spinodal decomposition process, whose dynamics is described by the Cahn-Hilliard equation.

## Spinodal decomposition and Cahn-Hilliard equation

Spinodal decomposition is a mechanism by which a mixture of two liquid or solid components A and B can rapidly unmix from a single thermodynamic phase into two coexisting phases, one A-rich and one B-rich, each with its own chemical composition and physical properties.

Spinodal decomposition is a continuous phase transition, whose order parameter is the concentration $c$ of one of the two mixture components, a locally-conserved quantity. The transition arises from small perturbations of the equilibrium concentration of the mixture, and is driven by a diffusion process of the mixture components. In fact, due to diffusion, A and B components start to form clusters until macroscopic A-rich and B-rich domains are formed, with subsequent formation of interfaces in the material. 
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
