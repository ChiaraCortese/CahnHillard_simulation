import numpy as np
import sys as sys
from chemical_potential_free_energy import chemical_potential, free_energy
from CahnHilliard_equation import Cahn_Hilliard_equation_integration
from create_initial_config import create_initial_config


# Microstructure geometry

N = 100               # number of subcells per cartesian direction -> grid of N-by-N subcells
dx = 1.               # dimension of subcell in x direction
dy = 1.               # dimension of subcell in y direction

#Material  specific parameters

M = 1.                # mobility
grad_coeff = 0.5      # gradient coefficient
A = 1.                # multiplicative constant of free energy

# Concentration parameters

c0 = 0.5              # initial equilibrium concentration
c_noise = 0.02        # perturbation amplitude -> IMPORTANT: should be an order of magnitude lower than c0

# Time integration parameters

t0 = 0.               # starting time
dt = 0.01             # time step
n_iterations = 5000   # number of time steps

# Build initial microstructure concentration grid

c = create_initial_config(N, c0, c_noise)

#compute initial free energy, average concentration and average chemical potential

average_chem_potential = np.sum(chemical_potential(c, A))/(N*N)
free_E = free_energy(c, A , grad_coeff, dx, dy)
average_c = np.sum(c)/(N*N)

#open file to write the simulated concentration data
data_config_file = open("Data/configurations.txt", "w")
column_names_string = "Time "
#write column names
for l in range(0, N):
    for j in range(0, N):
        column_names_string += "c"+str(l)+str(j)+" "
data_config_file.write(column_names_string+"\n")
#print initial concentration values
data_config_file.write(str(t0))
for l in range(0, N):
    for j in range(0, N):
        data_config_file.write(" "+str(c[l,j]))
data_config_file.write("\n")

#open file to write separately average concentration, average chem. potential and free energy
data_average_param_file = open("Data/average_parameters.txt", "w")
column_names_string = "Time AverageConcentration AverageChem.Potential FreeEnergy\n"
data_average_param_file.write(column_names_string)
#print initial values to file (with time indicator) 
string_to_print = str(t0)+" "+str(average_c)+" "+str(average_chem_potential)+" "+str(free_E)+"\n"
data_average_param_file.write(string_to_print)

# Perform time evolution with time step dt for n_iterations, 
# computing also average chem. potential, free energy, and average concentration

for i in range(1,n_iterations+1):
    #update time value
    t = t0 + i*dt
    #update concentration integrating Cahn-Hilliard equation
    c = Cahn_Hilliard_equation_integration(c, A, grad_coeff, dx, dy, M, dt)
    #print new configuration data to file (with time indicator)
    data_config_file.write(str(t))
    for l in range(0, N):
        for j in range(0, N):
            data_config_file.write(" "+str(c[l,j]))
    data_config_file.write("\n")
    #compute physical quantities of new configuration
    average_chem_potential = np.sum(chemical_potential(c, A))/(N*N)
    free_E = free_energy(c, A, grad_coeff, dx, dy)
    average_c = np.sum(c)/(N*N)
    #print physical quantities to file (with time indicator) 
    string_to_print = str(t)+" "+str(average_c)+" "+str(average_chem_potential)+" "+str(free_E)+"\n"
    data_average_param_file.write(string_to_print)
    #print simulation status on the command line
    sys.stdout.write("\r Simulation running: "+"{:.1f}".format(i/n_iterations*100)+"%")







