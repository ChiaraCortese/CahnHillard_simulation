import numpy as np
from chemical_potential_free_energy import chemical_potential
from concentration_laplacian import concentration_laplacian


def Cahn_Hilliard_equation_integration(c, A, k, dx, dy, M, dt):
    """This function performs time integration of the Cahn-Hilliard equation. 
    For a description of Cahn-Hilliard equation check the README.md
    
    Parameters: 
    c: N-by-N 2D array of floats
       input configuration
    A: float, not <0.
       multiplicative constant of chemical potential
    k: float, not <0.
       gradient coefficient
    dx, dy: floats, not <0. nor = 0.
           dimensions in x and y direction of a concentration subcell
    M: float, not <0.
       mobility of the concentration's particles
    dt: float, not <0.
        time step for time integration

    Returns: 
    c_updated: N-by-N 2D array
              concentration values updated according to Cahn-Hilliard equation"""

    #Check M and dt are valid input parameters (all the others are checked in the called functions)
    if M<0. or dt<0.:
         raise ValueError('M and dt parameters cannot be negative, check again the config.txt file description')

     #Compute chemical potential of current concentration configuration
    chem_potential = chemical_potential(c, A)   

    #Compute current gradient term of Cahn-Hilliard eq. : -2k*lap(c)
    gradient_term = 2*k*concentration_laplacian(c, dx, dy)

    #Compute concentration grid after time dt
    c_updated = c + dt*M*concentration_laplacian((chem_potential-gradient_term), dx, dy)

    #make sure output configuration is physical: reassign values lower than 0. to 0. and higher than 1. to 1.
    Ny, Nx = np.shape(c)
    for i in range(0,Nx):
        for j in range(0,Ny):
            if c_updated[j,i]<0. :
               c_updated[j,i] = 0.0
            if c_updated[j,i]>1. :
               c_updated[j,i] = 1.0
                
    return c_updated