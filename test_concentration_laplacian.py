import numpy as np
from concentration_laplacian import concentration_laplacian
from create_initial_config import create_initial_config
from hypothesis import given
import hypothesis.strategies as st
import pytest as pt

@given(N=st.integers(min_value=2, max_value=100), dx = st.floats(min_value=0.1), dy=st.floats(min_value=0.1), c = st.floats(min_value = 0, max_value=1))
def test_if_c_is_const_c_laplacian_is_0(N, dx, dy,c):
    """this function tests that if the input concentration N-by-N 2D array c is constant, the returned laplacian
       is still an N-by-N 2D array and its values are all zeros

       GIVEN: c = constant,N,dx,dy randomly picked numbers that do not invalidate function requirements 
       WHEN: they are provided as parameters to concentration_laplacian()
       THEN: function returs c_laplacian of shape (N,N) with all elements equal to zero"""
    
    c_constant=np.full((N,N), c)
    c_laplacian=concentration_laplacian(c_constant,dx,dy)
    assert np.shape(c_laplacian) == (N, N)
    for i in [0,N-1]:
      for j in [0,N-1]:
         assert  c_laplacian[i,j] == 0

@given(N=st.integers(min_value=2, max_value=100), dx=st.floats(max_value=0.), dy=st.floats(max_value=0.))
def test_initState_fails_for_incorrect_dxdy_parameters(N, dx, dy):
    """this function tests that if incorrect Nx, Ny parameters are given to create_initial_config(), 
       the function raises an error

       GIVEN: N randomly picked real numbers, dx, dy float numbers lower than 0
       WHEN: they are provided as parameters to concentration_laplacian()
       THEN: function raises ValueError"""
    
    c_0=0.5
    c_noise=0.02
    c=create_initial_config(N,c_0, c_noise)
    with pt.raises(ValueError):
       concentration_laplacian(c,dx,dy)


def test_concentration_laplacian_returns_correct_values():
    """this function tests that, given simple and integer array c0, the laplacian matrix 
       computed by concentration_laplacian() is equal to the expected one
       
       GIVEN : 3-by-3 matrix c0 of integer values, dx = 1, dy=1
       WHEN: they are provided as parameters to concentration_laplacian()
       THEN: function returns the values expected by handmade calculations
       """

    N = 3
    dx = 1.
    dy = 1.
    c0 = np.array([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]])
    c_laplacian_expected = np.array([[12, 9, 6],
                           [3, 0, 3],
                           [-6, -9, -12]])
    c_laplacian = concentration_laplacian(c0, dx,dy)
    for i in [0,N-1]:
        for j in [0,N-1]:
            assert  c_laplacian[i,j] == c_laplacian_expected[i,j]