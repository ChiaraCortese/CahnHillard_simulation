import numpy as np


def free_energy(c, A, k, dx, dy):
    """This function computes the free energy of the system as the sum of the homogeneous term and 
    of the gradient term of the generalized diffusion potential. 
    Check README.md for the physical meaning of the parameters
    
    Parameters:
    c: Ny-by-Nx array of float numbers 
       concentration field of 2D microstructure formed by Nx times Ny subcells
    A: float
       multiplicative constant
    k: float
       gradient coefficient
    dx: float
        dimension in x direction of a concentration subcell
    dy: float
        dimension in y direction of a concentration subcell
    
    Returns:
    free_energy: float
                 the total free energy of the concentration configuration"""
    
    
    #check validity of input parameters, validity of c already check in the create_initial_config() function
    if dx<=0. or dy<=0. or A<0. or k<0.:
        raise ValueError('dx, dy, A, k parameters cannot be negative, check again the config.txt file description')
    
    #retrieve shape of the c array
    Ny, Nx = np.shape(c)

    #compute homogeneous free energy term
    F_homogeneous = dx*dy*A*np.sum(c*c*(1-c)*(1-c))

    #compute gradient term using forward finite difference to compute the derivatives:
     #in first and last element of each row and column would not be possible to do finite difference derivative,
     #so use the element at the other edge of the supercell to compute the difference, 
     #as if the supercell was closed with opposite edges connected.
    c_y_minus_dy_elements = np.vstack([c[Ny-1,:],c[0:Ny-1,:]])
    c_x_minus_dx_elements = np.hstack([c[:,Nx-1].reshape((Nx,1)), c[:,0:Nx-1]])
    F_gradient = (k/(dx)**2)*np.sum((c-c_x_minus_dx_elements)**2) + (k/(dy)**2)*np.sum((c-c_y_minus_dy_elements)**2)

    free_energy = F_homogeneous + F_gradient

    return free_energy

def chemical_potential(c, A):
    """This function computes the chemical potential field of the concentration configuration c 
    as the analytical derivative of the free energy homogeneous term with respect to the concentration.
    
    Parameters:
    c: Ny-by-Nx array of float numbers 
       concentration field of 2D microstructure formed by Nx times Ny subcells
    A: float
       multiplicative constant
       
    Returns:
    chem_potential: Ny-by-Nx array of float numbers 
                    chemical potential field """
    if A<0.:
        raise ValueError('A must be positive, check the config.txt file description')

    chem_potential = 2*A*(c*((1-c)**2) - (c**2)*(1-c))

    return chem_potential

    