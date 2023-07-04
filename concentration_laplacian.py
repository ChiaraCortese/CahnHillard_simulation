import numpy as np

def concentration_laplacian(c, dx, dy):
    """This function calculates the laplacian of the concentration of a 2D microstructure 
       using second symmetric derivative: 
       lap(c) = (c(x+dx,y)+c(x-dx,y)-2c(x,y))/(dx*dx) + (c(x,y+dy)+c(x,y-dy)-2c(x,y))/(dy*dy)
       For the discrete microstructure that we simulate, dx, dy are equivalent to the subcell x and y dimensions
       while c(x+dx, y) is equivalent to concentration of the right of c(x,y) cell, 
       c(x, y+dy) is the concentration of the one below, considering cartesian axis with y axis pointing down, etc.
    
    Parameters:
    c: Ny-by-Nx array of float numbers 
       concentration field of 2D microstructure formed by Nx times Ny subcells
    dx: float
        dimension in x direction of a concentration subcell
    dy: float
        dimension in y direction of a concentration subcell
        
    Returns:
    c_laplacian: Nx-by-Ny array of float numbers
                 the laplacian of the microstructure concentration"""
    
    #check validity of input parameters, validity of c already check in the create_initial_config() function
    if dx<=0. or dy<=0.:
        raise ValueError('dx and dy parameters must be positive, check the config.txt file description')
    
    #create c_laplacian output array of same shape of c
    Ny, Nx = np.shape(c)
     
     #to simulate a periodic structure of unit cell equal to the simulated microstructure, for edge elements,
     #use the element at the other edge of the supercell to compute the difference, 
     #as if the supercell was closed with opposite edges connected
    c_y_plus_dy_elements = np.vstack([c[Ny-1,:],c[0:Ny-1,:]])
    c_y_minus_dy_elements = np.vstack([c[1:Ny,:],c[0,:]])
    c_x_plus_dx_elements = np.hstack([c[:, 1:Nx], c[:,0].reshape((Nx,1))])
    c_x_minus_dx_elements = np.hstack([c[:,Nx-1].reshape((Nx,1)), c[:,0:Nx-1]])
    
    #Reconstruct formula for symmetric second derivative
    c_laplacian = (c_x_minus_dx_elements + c_x_plus_dx_elements - 2*c)/(dx*dx)

    c_laplacian += (c_y_minus_dy_elements + c_y_plus_dy_elements-2*c)/(dy*dy)


    return c_laplacian