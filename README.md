# Simulating a spinodal decomposition process governed by Cahn-Hilliard equation

This repository contains the material produced for the exam "Software and Computing for Applied Physics" - University of Bologna. It consists of a simulation of a spinodal decomposition process, whose dynamics is described by the Cahn-Hilliard equation.

## Spinodal decomposition and Cahn-Hilliard equation

Spinodal decomposition is a mechanism by which a mixture of two liquid or solid components A and B can rapidly unmix from a single thermodynamic phase into two coexisting phases, one A-rich and one B-rich, each with its own chemical composition and physical properties.

Spinodal decomposition is a continuous phase transition, whose order parameter is the concentration $c$ of one of the two mixture components, a locally-conserved quantity. The transition arises in materials with a miscibility gap, meaning that small, local perturbations of the equilibrium concentration of the homogeneous mixture can cause the system to develop local clusters of A or B components until macroscopic A-rich and B-rich domains are formed. The different domains are separated by *diffusion interfaces*, characterized by the presence of a concentration gradient. 
The transition is driven by a diffusion process of the mixture components that aims to minimize the system's free energy.  
Given a mixture of two components A and B, with concentrations respectively $(1-c(\vec r))$ and $c(\vec r)$, when subjected to a local concentration perturbation, the diffusion process of species B is described by the following diffusion equation:
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

For more info on Cahn-Hilliard equation and spinodal decomposition, check [this](https://doi.org/10.1002/0471749311.ch18).

For more info on phase-field modeling, check [this](https://doi.org/10.1146/annurev.matsci.32.112001.132041)

### Numerical integration of the Cahn-Hilliard equation

In this project, I modeled a 2D microstructure as

## Structure of the project

The project is divided into 5 blocks:
- the [simulation_configuration.txt](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/simulation_configuration.txt) file, where I inserted all the simulation parameters customizable by the user (further discussion is the next section), so that if the user wants to run the simulation with different parameters, it is sufficient to modify the configuration file without changing the simulation main code
- the [create_initial_config.py], which hosts a homonymous function returning a 2D array whose elements represent the values of the initial concentration grid.
- the [chemical_potential_free_energy.py], [concentration_laplacian.py], where I wrote the functions dedicated to computing the laplacian of the concentration grid and to compute the free energy and the chemical potential as described above
- the [simulation.py], the core part of the simulation, where the simulation configuration parameters are read using ConfigParser,  

## How to run the simulation and plot the results 

To successfully run the simulation, follow these steps:
1. Configure the simulation by changing the [simulation_configuration.txt](https://github.com/ChiaraCortese/CahnHilliard_simulation/main/simulation_configuration.txt) file. The file hosts all the values of the parameters introduced in the previous section, plus the local paths where the simulated data and the images will be stored:
   - N: number of subcells per grid dimension, must be an integer number >2
   - dx, dy: dimensions of the single subcells, must be positive float numbers
   - M: average mobility of the B species, must be a non-negative float number
   - grad_coefficient: coefficient of the gradient term of the generalized diffusion potential, must be a non-negative float number
   - A: multiplicative coefficient of the free energy, must be a non-negative float number
   - c0: unperturbed concentration, must be a float number in [0,1]
   - c_noise: amplitude of the random perturbation, should be an order of magnitude lower than c0, and in any case a float number in [0,1]
   - t0: initial time of the simulation, must be a non-negative float number
   - dt: time step in the Cahn-Hilliard equation integration, must be a non-negative float number
   - n_iterations: number of time steps to be performed during the simulation, must be an integer
   - c_config_datasave: path and filename to store the simulated concentration grid values
   - aver_quantities_datasave: path and filename to store the simulated free energy, average concentration and average chemical potential
   - initial_c_grid_pic: path and filename to save the initial concentration grid picture
   - final_c_grid_pic: path and filename to save the final concentration grid picture
   - other_variables_pic: path and filename to save the graphs of free energy, average chemical potential, and average concentration vs. time
3. To launch the simulation from the command line, use the syntax **python simulation.py simulation_configuration.txt**. The configuration parameters will be read from the simulation_configuration.txt file using ConfigParser.
4. To visualize the results of the simulation, launch from the command line the plot file using the syntax **python plots.py simulation_configuration.txt**. The concentration grid pictures will be shown one after another in an animation, to illustrate the changes during time evolution, with only the first and last pictures saved as .jpg images. The free energy, average chemical potential, and average concentration will be plotted as functions of time and saved in a separate file.


## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
