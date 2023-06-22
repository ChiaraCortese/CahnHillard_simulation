import numpy as np


def create_initial_config(Nx, Ny, c_0, c_noise):
    """This method generates a supercell of dimensions Nx*Ny, formed by subcells of composition
    given by c_0 plus a random fluctuation.
       
    Parameters
        Nx : number of cells in x direction.
        Ny : number of cells in y direction.
        c_0: unperturbed concentration
        c_noise: concentration fluctuation 
    
    Returns:
        The state of the initial configuration of the Nx*Ny supercell. 
        
    Raise:
        ValueError if length or width of the lattice dimensions is less than 1, if C_0 or c_noise 
        are not in [0,1], or if any of the initialized subcells' concentration is not in [0,1]"""

    if Nx < 1 or Ny < 1:
        raise ValueError('Both dimensions of the lattice must be > 1, but are {} and {}'.format(Nx,Ny))
    if c_0 < 0 or c_0 > 1:
        raise ValueError('Unperturbed concentration must be >0, but is {}'.format(c_0))
    np.random.seed(1)
    initState = c_0 + c_noise*(0.5-p.random.rand(Nx, Ny)) 
    if initState < 0 or initState > 1:
        raise ValueError('Invalid combination of c_0 and c_noise: negative concentration values were generated')
    return initState