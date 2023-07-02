import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import time as time

"---------------------------------IMPORT CONCENTRATION DATA FROM FILES-----------------------------------------"
#Read concentration data from file
concentration_evolution = np.loadtxt("Data/configurations.txt", skiprows=1)

#Separate time indicator
t = concentration_evolution[:, 0]

#Retrieve information on number of time steps and concentration grid shape
n_iterations, N = np.shape(concentration_evolution)       

#Remember that N = Nx*Ny + 1, with Ny = Nx; compute Nx
Nx = int(np.sqrt(N - 1))
c = concentration_evolution[:,1:N].reshape(n_iterations,Nx,Nx)
"--------------------------------------PLOT CONCENTRATION DATA-------------------------------------------------"
#Create figure and subplot
fig = plt.figure()
ax = fig.add_subplot(111)

#Plot initial concentration grid on a 2D regular raster
im = ax.imshow(c[0], cmap='bwr', interpolation=None)

# create an Axes on the right side of ax. The width of cax will be 5%
# of ax and the padding between cax and ax will be fixed at 0.05 inch.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)

#Plot colorbar on the right of the concentration grid
plt.colorbar(im, cax)

#Set plot title
ax.set_title("Concentration grid: t = "+"{:.2f}".format(t[0]))

#Save initial configuration as .jpg image

plt.savefig('Images/initial_concentration_grid.jpg')

#Enable interactive mode and show plot
plt.ion()
plt.show()

for i in range(1,n_iterations+1):
    #Update concentration grid plot data
    im.set_data(c[i])
    #
    ax.set_title("Concentration grid: t = "+"{:.2f}".format(t[i]))
    #redraw figure
    fig.canvas.draw_idle()
    # flush GUI events
    fig.canvas.flush_events()
    #Pause
    time.sleep(0.01)

#Save final concentration grid
plt.savefig('Images/final_concentration_grid.jpg')

"-------------------------------------IMPORT SYSTEM AVERAGE QUANTITIES DATA---------------------------------"
#Read free energy, average chem. potential and averge concentration data from file
t, average_c, average_chem_potential, free_energy = np.loadtxt("Data/configurations.txt", skiprows=1, unpack=True)

"----------------------------------------PLOT AVERAGE QUANTITIES DATA --------------------------------------"
#Create figure and subplots
fig1, axs = plt.subplots(2,2)
