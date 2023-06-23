import numpy as np
from numpy.random import rand

def create_initial_config(Nx, Ny, c_0, c_noise):
    """This method generates a supercell of dimensions Nx*Ny, formed by subcells of composition
    given by c_0 plus a random fluctuation.
       
    Parameters:
        Nx : int
             number of cells in x direction.
        Ny : int
              number of cells in y direction.
        c_0: float
             unperturbed concentration
        c_noise: float
             concentration fluctuation 
    
    Returns:
        initState: Nx-by-Ny array
        The state of the initial configuration of the Nx*Ny supercell. 
        
    Raise:
        ValueError if the supercell dimensions are less than 1 or not integer numers, if C_0 or c_noise 
        are not in [0,1], or if any of the initialized subcells' concentration is not in [0,1]"""
    
    #check validity of input parameters
    if not isinstance(Nx, int) or not isinstance(Ny, int):
        raise TypeError('Nx or Ny values must be integer numbers.')
    if Nx < 1 or Ny < 1:
        raise ValueError('Both dimensions of the lattice must be > 1.')
    if c_0 < 0 or c_0 > 1:
        raise ValueError('Unperturbed concentration must be in [0,1].')
    if c_noise < 0 or c_noise > 1:
        raise ValueError('Concentration fluctuation must be in [0,1].')

    #make the initial configuration repeatable
    np.random.seed(1)
    
    #create initial configuration with noise described by uniform distribution of mean value c_noise
    initState = c_0 + c_noise*(0.5-rand(Nx, Ny)) 
    
    #check validity of initial configuration
    for c in initState:
        for cc in c:
            if cc<0 or cc>1:
                raise ValueError('Invalid combination of c_0 and c_noise: negative concentrations occurred')
    
    return initState