import numpy as np
import sys as sys
import configparser as cp
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import time as time

"-----------------------------------IMPORT IMAGES PATHS------------------------------------------"
#Import configuration parameters from simulation_configuration.txt file
config = cp.ConfigParser()
config.read(sys.argv[1])

# Destinations for image saving
initial_c_grid_pic = config.get('image_paths', 'initial_c_grid_pic')
final_c_grid_pic = config.get('image_paths', 'final_c_grid_pic')
other_variables_pic = config.get('image_paths', 'other_variables_pic')

# Data files paths
c_grid_datasave = config.get('data_paths', 'c_config_datasave')
aver_quantities_datasave = config.get('data_paths', 'aver_quantities_datasave')

"---------------------------------IMPORT DATA FROM FILES-----------------------------------------"
#Read concentration data from file
concentration_evolution = np.loadtxt(c_grid_datasave, skiprows=1)

#Separate time indicator
t_concentration = concentration_evolution[:, 0]

#Retrieve information on number of time steps and concentration grid shape
n_iterations, N = np.shape(concentration_evolution)       

#Remember that N = Nx*Ny + 1, with Ny = Nx; compute Nx
Nx = int(np.sqrt(N - 1))
#Re-arranger concentration values in grid format
c = concentration_evolution[:,1:N].reshape(n_iterations,Nx,Nx)

#Read average quantities data from file
t_average, average_c, average_chem_potential, free_energy = np.loadtxt(aver_quantities_datasave, skiprows=1, unpack=True)

"--------------------------------------PLOT CONCENTRATION DATA-------------------------------------------------"
#Create figure and subplot
fig = plt.figure()
ax1 = fig.add_subplot(111)

#Set figure title
fig.suptitle('Spinodal decomposition', fontsize=16)
#Plot initial concentration grid on a 2D regular raster
im = ax1.imshow(c[0], cmap='bwr', interpolation=None)

# create an Axes on the right side of ax. The width of cax will be 5%
# of ax and the padding between cax and ax will be fixed at 0.05 inch.
divider = make_axes_locatable(ax1)
cax = divider.append_axes("right", size="5%", pad=0.05)

#Plot colorbar on the right of the concentration grid
plt.colorbar(im, cax)

#Set concentration plot title
ax1.set_title("Concentration grid: t = "+"{:.2f}".format(t_concentration[0])+" arb.units")

#Save initial configuration as .jpg image

plt.savefig(initial_c_grid_pic)

#Enable interactive mode and show plot
plt.ion()
plt.show()

for i in range(1,n_iterations):
    #Update concentration grid plot data
    im.set_data(c[i])
    #Update concentration plot title
    ax1.set_title("Concentration grid: t = "+"{:.2f}".format(t_concentration[i])+" arb.units")
    #redraw figure
    fig.canvas.draw_idle()
    # flush GUI events
    fig.canvas.flush_events()
    #Pause
    time.sleep(0.001)

#Save final concentration grid
plt.savefig(final_c_grid_pic)

"-----------------------------------------PLOT AVERAGE QUANTITIES-------------------------------------"

#Create new figure and subplots

fig, axs = plt.subplots(3, sharex=True, figsize=(7,10))

#Set figure title
fig.suptitle('Spinodal decomposition', fontsize=16)

#Plot free energy vs. time
axs[0].scatter(t_average, free_energy, c="blue")
#Set axis and title
axs[0].set_title("Free energy time evolution")
axs[0].set_xlabel("Time (arb.units)")
axs[0].set_ylabel("Free energy (arb.units)")

#Plot average concentration vs. time
axs[1].scatter(t_average, average_c, c="green")
#Set axis and title
axs[1].set_title("Average concentration time evolution")
axs[1].set_xlabel("Time (arb.units)")
axs[1].set_ylabel("Average concentration")

#Plot average chemical potential vs. time
axs[2].scatter(t_average, average_chem_potential, c="red")
#Set axis and title
axs[2].set_title("Average chemical potential time evolution")
axs[2].set_xlabel("Time (arb.units)")
axs[2].set_ylabel("Average chem. potential (arb.units)")

#Save plots
plt.savefig(other_variables_pic)
