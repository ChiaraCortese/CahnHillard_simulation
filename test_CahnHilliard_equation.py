import numpy as np
from create_initial_config import create_initial_config
from chemical_potential_free_energy import chemical_potential
from concentration_laplacian import concentration_laplacian
from CahnHilliard_equation import Cahn_Hilliard_equation_integration
from hypothesis import given
import hypothesis.strategies as st
import pytest as pt

@given(dx=st.floats(min_value=0.1), dy=st.floats(min_value=0.1), k=st.floats(min_value=0.), A=st.floats(min_value=0.), M=st.floats(max_value = -0.001), dt=st.floats(max_value=-0.001))
def test_CahnHilliard_integration_fails_with_incorrect_M_dt_parametes(dx,dy,k,A, M, dt):
    """this function tests that if invalid M, dt parameters are given to Cahn_Hilliard_equation_integration(), 
       the functions raise an error

       GIVEN: A, k,dx, dy valid float numbers, a given concentration matrix c, negative M, dt
       WHEN: they are provided as parameters to Cahn_Hilliard_equation_integration()
       THEN: function raises ValueError"""
    N = 10
    c_0=0.5
    c_noise=0.02
    c=create_initial_config(N,c_0, c_noise)
    with pt.raises(ValueError):
       Cahn_Hilliard_equation_integration(c, A, k, dx, dy, M, dt)

def test_CahnHilliard_integration_returns_correct_values():
     """this function tests that, given a precise concentration grid, Cahn_Hilliard_equation_integration() 
    returns the correct updated concentration value for each subcell, in an array of same shape of the input concentration one 
    
    GIVEN: a 2-by-2 concentration grid with either 0 or 1 values, and A=1,M=1, k=1, dx=1, dy=1
    WHEN: they are provided as input parameters to Cahn_Hilliard_equation_integration(),
    THEN: function returns a 2-by-2, 2D array with all elements equal to manually computed values"""

     N = 2
     A = 1
     dx = 1
     dy = 1
     k = 1
     c = np.array([[1, 0],
                  [0, 1]])
     updated_c_computed = Cahn_Hilliard_equation_integration(c, A, k, dx, dy, M, dt)
     updated_c_expected = np.array([[0, 0],
                              [0, 0]])
     assert np.shape(updated_c_computed) == np.shape(c)
     for i in [0,N-1]:
         for j in [0,N-1]:
             assert updated_c_computed[i,j] == updated_c_expected[i,j]