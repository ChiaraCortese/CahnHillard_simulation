import numpy as np
from create_initial_config import create_initial_config
from chemical_potential_free_energy import free_energy, chemical_potential, average_chemical_potential_and_concentration
from hypothesis import given
import hypothesis.strategies as st
import pytest as pt

@given(dx=st.floats(max_value=0.), dy=st.floats(max_value=0.), k=st.floats(max_value=0.), A=st.floats(max_value=0.))
def test_chemical_potential_and_free_energy_fail_with_incorrect_parameters(dx,dy,k,A):
    """this function tests that if invalid dx,dy,k, A parameters are given to free_energy() and chemical_potential(), 
       the functions raise an error

       GIVEN: A, k,dx, dy float numbers lower than 0 and a given concentration matrix c
       WHEN: they are provided as parameters to chemical_potential() and free_energy()
       THEN: function raises ValueError"""
    N = 10
    c_0=0.5
    c_noise=0.02
    np.random.seed(1)
    c=create_initial_config(N,c_0, c_noise)
    with pt.raises(ValueError):
       free_energy(c,A,k,dx,dy)
       chemical_potential(c,A)

@given(A=st.floats(min_value=0.1), N = st.integers(min_value=2, max_value=100))
def test_chemical_potential_returns_array_of_same_shape_of_input_array(A, N):
    """this function tests that chemical_potential() returns an array of shape equal 
    to the input concentration c.
    TEST WRITTEN AFTER THE FUNCTION RETURNED AN ARRAY OF INCORRECT SHAPE, 
    KEEP THE TEST TO CHECK THAT THE ERROR DOES NOT REOCCUR 
    
       GIVEN: A positive float number A, c elements all equal to 0.5, supercell of dimension N-by-N
       WHEN: they are provided as parameters to chemical_potential()
       THEN: chemical_potential() returns an array of shape (N,N)"""
    c_0=0.5
    c_noise=0.02
    np.random.seed(1)
    c=create_initial_config(N,c_0, c_noise)
    chem_potential = chemical_potential(c, A)
    assert np.shape(chem_potential) == (N, N)

def test_free_energy_returns_float_number():
    """this function tests that free_energy() returns a single float number
    TEST WRITTEN AFTER THE FUNCTION RETURNED AN ARRAY INSTEAD OF A SINGLE FLOAT NUMBER, 
    KEEP THE TEST TO CHECK THAT THE ERROR DOES NOT REOCCUR AGAIN
    
    GIVEN: random valid dx, dy, k, A parameters, and a given concentration config. c
    WHEN: they are provided as parameters to free_energy
    THEN: free_energy() returns a single float number"""
    dx=1.
    dy=1.
    k=0.5
    A=1.
    N = 10
    c_0=0.5
    c_noise=0.02
    np.random.seed(1)
    c=create_initial_config(N,c_0, c_noise)
    F = free_energy(c,A,k,dx,dy)
    assert isinstance(F, float)


def test_chemical_potential_returns_expected_values():
    """this function tests that, given a precise concentration grid, chemical_potential() 
    returns the correct chemical potential value for each subcell 
    
    GIVEN: a 2-by-2 concentration grid with either 0 or 1 values, and A=1,
    WHEN: they are provided as input parameters to chemical_potential(),
    THEN: chemical_potential() returns a 2-by-2, 2D array with all elements equal to zero"""

    N = 2
    A = 1
    c = np.array([[1, 0],
                  [0, 1]])
    chem_pot_computed = chemical_potential(c, A)
    chem_pot_expected = np.array([[0, 0],
                              [0, 0]])
    assert np.array_equal(chem_pot_computed, chem_pot_expected)

def test_free_energy_returns_expected_value():
    """this function tests that, given a precise concentration grid, free_energy() 
    returns the correct free energy value of the system 
    
    GIVEN: a 2-by-2 concentration grid with either 0 or 1 values, and A=1, k=1, dx=dy=1,
    WHEN: they are provided as input parameters to free_energy(),
    THEN: free_energy() returns a float that is exactly equal to the manually calculated  value"""
    
    N = 2
    A = 1
    k = 1
    dx = 1
    dy = 1
    c = np.array([[1, 0],
                  [0, 1]])
    free_energy_computed = free_energy(c, A, k, dx, dy)
    free_energy_expected = 8
    assert free_energy_computed == free_energy_expected

def test_average_chemical_potential_and_concentration_returns_expected_value():
    """this function tests that, given precise chemical potential and concentration grids, 
    average_chemical_potential_and_concentration() returns the correct values for the average chemical potential 
    and the average concentration of the system 
    
    GIVEN: a chemical potential grid and a concentration grid of shape (N,N), N=2
    WHEN: they are provided as input parameters to average_chemical_potential_and_concentration(),
    THEN: average_chemical_potential_and_concentration() returns two floats that are exactly equal to the 
          manually calculated values (with a tolerance of 1e-8, necessary since two floats are compared)"""

    chem_pot_grid = [[2.,4.],
                     [4.,2.]]
    c_grid = [[0.1, 0.3],
              [0.3, 0.1]]
    N = 2

    expected_average_chem_value = 3.
    expecte_c_value = 0.2
    computed_average_chem_value, computed_c_value = average_chemical_potential_and_concentration(c_grid, chem_pot_grid, N)
    assert np.allclose(expected_average_chem_value, computed_average_chem_value, rtol=1e-8)
    assert np.allclose(expecte_c_value, computed_c_value, rtol=1e-8)

    

