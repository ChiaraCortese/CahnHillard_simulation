import numpy as np
from create_initial_config import create_initial_config
from hypothesis import given
import hypothesis.strategies as st
import pytest as pt

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

@given(c_0=st.floats(min_value=0, max_value=1), c_noise=st.floats(min_value=0, max_value=1), Nx = st.floats(), Ny=st.floats())
def test_initState_fails_for_incorrect_NxNy_parameters(c_0, c_noise, Nx, Ny):
    """this function tests that if incorrect Nx, Ny parameters are given to create_initial_config(), 
       the function raises an error

       GIVEN: Nx,Ny randomly picked real numbers 
       WHEN: they are provided as parameters to create_initial_config()
       THEN: function raises TypeError"""
    with pt.raises(TypeError):
       create_initial_config(Nx,Ny,c_0,c_noise)

@given(c_0=st.floats(min_value=1.1), c_noise=st.floats(max_value=1.1), Nx = st.integers(max_value=100), Ny=st.integers(max_value=100))
def test_initState_fails_for_incorrect_c0cnoise_parameters(c_0, c_noise, Nx, Ny):
    """this function tests that if incorrect c_0, c_noise parameters are given to create_initial_config(), 
       the function raises an error

       GIVEN: c_0, c_noise randomly picked real numbers 
       WHEN: they are provided as parameters to create_initial_config()
       THEN: function raises ValueError"""
    with pt.raises(ValueError):
       create_initial_config(Nx,Ny,c_0,c_noise)

@given(c_0=st.floats(min_value=0, max_value=1), c_noise=st.floats(min_value=0, max_value=1))
def test_initState_fails_for_null_cell_parameters(c_0, c_noise):
    """this function tests that create_initial_config(), 
       the function raises an error for Nx=0, Ny=0

       GIVEN: null supercell dimensions parameters 
       WHEN: they are provided as parameters to create_initial_config()
       THEN: function raises ValueError"""
    Nx=0
    Ny=0
    with pt.raises(ValueError):
       create_initial_config(Nx,Ny,c_0,c_noise)