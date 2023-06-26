import numpy as np
from numpy.random import rand

def create_initial_config(N, c_0, c_noise):
    """This method generates a 2D supercell of dimensions N*N, formed by subcells of composition
    given by c_0 plus a random fluctuation.
       
    Parameters:
        N : int
             number of cells in x and y direction, must be at least =2.
        c_0: float
             unperturbed concentration
        c_noise: float
             concentration fluctuation 
    
    Returns:
        initState: N-by-N 2D array
        The state of the initial configuration of the Nx*Ny supercell, represented by a grid of N columns and N rows. 
        
    Raise:
        ValueError if the supercell dimensions are less than 1 or not integer numers, if C_0 or c_noise 
        are not in [0,1], or if any of the initialized subcells' concentration is not in [0,1]"""
    
    #check validity of input parameters
    if not isinstance(N, int):
        raise TypeError('Nx or Ny values must be integer numbers.')
    if N < 2:
        raise ValueError('Both dimensions of the lattice must be > 1.')
    if c_0 < 0 or c_0 > 1:
        raise ValueError('Unperturbed concentration must be in [0,1].')
    if c_noise < 0 or c_noise > 1:
        raise ValueError('Concentration fluctuation must be in [0,1].')

    #make the initial configuration repeatable
    np.random.seed(1)
    
    #create initial configuration with noise described by uniform distribution of mean value c_noise;
    #rand(d_0, d_1) returns array with d_0 rows and d_1 columns, 
    #so to represent real space configuration with cartesian x and y axis, use d_0_Ny, d_1=Nx.
    initState = c_0 + c_noise*(0.5-rand(N, N)) 
    
    #check validity of initial configuration
    for c in initState:
        for cc in c:
            if cc<0 or cc>1:
                raise ValueError('Invalid combination of c_0 and c_noise: negative concentrations occurred')
    
    return initState