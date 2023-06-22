import numpy as np
from create_initial_config import create_initial_config
from hypothesis import given
import hypothesis.strategies as st

@given(Nx=st.integers(min_value=1, max_value=100), Ny=st.integers(min_value=1, max_value=100), c_0=st.floats(min_value=0, max_value=1))
def test_initState_is_c_0_if_noise_is_0(Nx, Ny, c_0):
    """this function tests that if c_noise is null, the initial configuration 
       is an array of Nx-by-Ny c_0

       GIVEN: c_noise=0,Nx,Ny,c_0 randomly picked numbers 
       WHEN: they are provided as parameters to create_initial_config()
       THEN: function returs initState with all elements equal to c_0"""

    c_noise=0.
    constant_array=np.full((Nx,Ny), c_0)
    initial_config=create_initial_config(Nx,Ny,c_0, c_noise)
    assert  initial_config.all()== constant_array.all()


    