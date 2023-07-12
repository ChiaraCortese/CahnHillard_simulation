import numpy as np
from create_initial_config import create_initial_config
from chemical_potential_free_energy import chemical_potential
from concentration_laplacian import concentration_laplacian
from CahnHilliard_equation import Cahn_Hilliard_equation_integration
from hypothesis import given, settings
import hypothesis.strategies as st
import pytest as pt

@settings(deadline=None)
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

def test_CahnHilliard_integration_returns_expected_values():
     """this function tests that if the initial concentration is the equilibrium one,
       Cahn_Hilliard_equation_integration() returns as the updated concentration value the initial one,
       for each subcell, in an array of same shape of the input concentration one 
    
    GIVEN: a 2-by-2 concentration grid with all values equal to 0.5, and A=1,M=1, k=1, dx=1, dy=1, dt=1
    WHEN: they are provided as input parameters to Cahn_Hilliard_equation_integration(),
    THEN: function returns a 2-by-2, 2D array with all elements equal to initial values"""

     N = 2
     A = 1
     dx = 1
     dy = 1
     k = 1
     M = 1
     dt = 1
     c = np.array([[0.5, 0.5],
                  [0.5, 0.5]])
     updated_c_computed = Cahn_Hilliard_equation_integration(c, A, k, dx, dy, M, dt)
     updated_c_expected = np.array([[0.5, 0.5],
                              [0.5, 0.5]])
     assert np.array_equal(updated_c_computed, updated_c_expected)

def test_CahnHilliard_integration_return_physical_output_configuration():
    """This function tests that if the concentration configuration obtained by integrating the 
    Cahn-Hilliard equation turns out to be out of bound, like lower than 0 or higher than 1, 
    then the function automatically rescale the out-of-bound value to 0 or 1 without raising errors.
    TEST WRITTEN AFTER FUNCTION RETURNING OUT-OF-BOUND CONCENTRATION VALUES FOR SPECIFIC INPUT VALUES, 
    KEEP TO CHECK THAT THIS PROBLEM DO NOT REOCCUR
    
    GIVEN: 2-by-2 concentration grid with a big concentration difference ([[0, 1], [1, 0]]), 
           A = k = dx = dy = M = dt = 1
    WHEN: they are provided as parameters to Cahn_Hilliard_equation_integration()
    THEN: function produces values out of bound that are automatically rescaled to physical values, 
          and output configuration is a physical one (with no concentration values out of [0, 1])"""

    N = 2
    A = 1
    dx = 1
    dy = 1
    k = 1
    M = 1
    dt = 1
    c = np.array([[0, 1], 
                 [1, 0]])
    updated_c = Cahn_Hilliard_equation_integration(c, A, k, dx, dy, M, dt)
    updated_c_validity = np.logical_and(updated_c>=0, updated_c<=1)
    assert updated_c_validity.all()
