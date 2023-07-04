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
where $k$ is a coefficient depending on the species involved, while $\mu$ was substitued using its relation with the free energ density $f^{hom}$ of the homogeneous mixture case. As for the system free energy $F$, its relation with $f^{hom}$ and $\vec \nabla c(\vec r)$ is:
$$F = \int_{volume} \Bigl[ f^{hom}(c) + k(\vec \nabla c)^2\Bigr] dV$$

Since the $c$ is a locally-conserved quantity, the continuity equation also holds:
$$\frac{\partial c}{\partial t} + \vec{\nabla} \cdot \vec{J}_B = 0.$$

By combining the diffusion and continuity equations, we obtain the **Cahn-Hilliard equation**:
$$\frac{\partial c}{\partial t} = \vec{\nabla} \cdot \Bigl\lbrace M\vec{\nabla} \Bigl( \frac{\partial f^{hom}}{\partial c} - 2k\nabla^2 c(\vec r)\Bigr)\Bigr\rbrace.$$

This derivation relies on phase-field modeling: with this method, a microstructure with compositional and/or structural domains, and thus interfaces, is described as a whole with a set of field variables. The field variables are assumed to be continuous across the interfacial regions. Common field variables are the local composition and the interface orientation.
In this simulation, only the local composition will be considered as a phase variable.

For more info on Cahn-Hilliard equation and spinodal decomposition, check [this](https://doi.org/10.1002/0471749311.ch18).

For more info on phase-field modeling, check [this](https://doi.org/10.1146/annurev.matsci.32.112001.132041)

### Numerical integration of the Cahn-Hilliard equation

In this project, I modeled a 2D microstructure as an N-by-N grid of subcells, each of dimensions $dx$ and $dy$. Each subcell was initiated to a random value $c$ in [ $c_0 -c_{noise}$ , $c_0 +c_{noise}$], where $c_0$ is the unperturbed concentration value and $c_{noise}$ the amplitude of the perturbation. To compute the free energy, I used the following expression:
$$F = F_{hom} + F_{grad},$$
with
$$F_{hom}= A \sum_{i=1}^N \sum_{j=1}^N dx \cdot dy \cdot c_{ij}^2 (1-c_{ij})^2,$$
where $A$ is a multiplicative constant and the indices $i,j$ identify a specific grid subcell, and
$$F_{grad} = k \Bigl[ \sum_{j=1}^N \sum_{i=1}^N \Bigl(\frac{c_{i, j}-c_{i-1, j}}{dx}\Bigr)^2 + \sum_{i=1}^N \sum_{j=1}^N \Bigl(\frac{c_{i, j}-c_{i, j-1}}{dy}\Bigr)^2 \Bigr],$$
where the gradient was computed using the finite difference method, and periodic boundary conditions were applied to the grid edges' values to simulate a periodic 2D structure with a unit cell equal to the microstructure.
The chemical potential grid was computed directly from the homogeneous free energy density:
$$\mu_{i,j} = \frac{\partial f^{hom}}{\partial c_{i,j}} = 2A\Bigl(c_{i,j}(1-c_{i,j})^2 - c_{i.j}^2(1-c_{i,j})\Bigr).$$

As for the laplacian of the concentration grid, the symmetric finite difference method was used:
$$\nabla^2 c_{i,j} = \frac{c_{i+1,j}+ c_{i-1,j}-2c_{i,j}}{dx^2} + \frac{c_{i,j+1}+ c_{i,j-1}-2c_{i,j}}{dy^2}.$$

All of this was then combined to numerically integrate the Cahn-Hilliard equation for each subcell microstructure:
$$c_{i,j} (t+dt) = c_{i,j}(t) + dt \cdot M \nabla^2 \Bigl[ \mu_{i,j}(t) - 2k\nabla^2 c_{i,j}(t)\Bigr], $$
where the laplacian of the quantity in square brackets was computed with the same method used for the concentration one.

## Structure of the project

The project is divided into 7 blocks:
- the [simulation_configuration.txt](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/simulation_configuration.txt) file, where I inserted all the simulation parameters customizable by the user (for a complete description, see the next section) so that if the user wants to run the simulation with different parameters, it is sufficient to modify the configuration file without changing the simulation main code;
- the [create_initial_config.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/create_initial_config.py), which hosts a homonymous function returning a 2D array whose elements represent the values of the initial concentration grid;
- the [chemical_potential_free_energy.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/chemical_potential_free_energy.py), [concentration_laplacian.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/concentration_laplacian.py), where I wrote the functions dedicated to computing the laplacian of the concentration grid and to compute the free energy and the chemical potential as described in the previous section;
- the [CahnHilliard_equation.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/CahnHilliard_equation.py), which hosts the Cahn_Hilliard_equation_integration() function that, when given as input parameters a concentration grid, together with $M$, $k$, $A$, $N$, $dx$ and $dy$, and $\Delta t$, returns the configuration grid after a time $\Delta t$ obtained by integrating the Cahn-Hilliard equation as described in the previous section. For the integration, the functions in [chemical_potential_free_energy.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/chemical_potential_free_energy.py), [concentration_laplacian.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/concentration_laplacian.py) are imported. The separation of the files into different functions was done to test them separately.
- the testing: each of the files cited above has a dedicated test, to ensure that all my functions work properly. I used hypothesis testing and checked the coverage with pytest-cov (reached coverage: 100%).
- the [simulation.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/simulation.py), the core part of the simulation, where the simulation configuration parameters are read using ConfigParser, uses them to initialize the concentration grid through [create_initial_config.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/create_initial_config.py), and computes its free energy, average concentration, and average chemical potential using the functions in [chemical_potential_free_energy.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/chemical_potential_free_energy.py). Then, for each time step required by the user, it updates the computed values by calling the Cahn_Hilliard_equation_integration() and then recomputes the average values and free energy. From the initial configuration until the last one, all the concentration grid values are stored in a local dedicated file together with the time indication. The average quantities and free energy are saved in a separate local file, always with a time indication.
- the [plots.py](https://github.com/ChiaraCortese/CahnHilliard_simulation/blob/main/plots.py), which retrieves from the local files the simulation data and:
  1. plots all the concentration grid values as 2D images with a color scale to represent if the concentration value of a subcell is above or below the unperturbed concentration value. The images are plotted in interactive mode, so that the user can see in the GUI the time evolution of the grid values as an animation;
  2. saves as .jpg files the initial and final concentration grid images
  3. saves as a single .jpg file the free energy, average concentration, and average chemical potential vs. time plots.

## How to run the simulation and plot the results 

To successfully run the simulation, follow these steps:
1. Configure the simulation by changing the [simulation_configuration.txt](https://github.com/ChiaraCortese/CahnHilliard_simulation/main/simulation_configuration.txt) file. The file hosts all the values of the parameters introduced in the previous section, plus the local paths where the simulated data and the images will be stored:
   - N: number of subcells per grid dimension, must be an integer number >2
   - dx, dy: dimensions of the single subcells, must be positive float numbers (and in general better to keep them =1.0)
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

Here is an example of the results obtained by running the simulation with the configuration in simulation_configuration.txt:
1) Initial and final configuration

   <img src="/Images/initial_concentration_grid.jpg" alt="Initial concentration grid" style="height: 240px; width:320px;"/>
   <img src="/Images/final_concentration_grid.jpg" alt="Final concentration grid" style="height: 240px; width:320px;"/>

3) Time evolution of free energy, average chemical potential and average concentration
   
   <img src="/Images/average_quantities_time_evol.jpg" alt="Average quantities time evolution" style="height: 500px; width:350px;"/>
Note that as expected, the simulated spinodal decomposition process maintained the average concentration constant, thus conserving the order parameter, and it minimized the free energy.

## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
