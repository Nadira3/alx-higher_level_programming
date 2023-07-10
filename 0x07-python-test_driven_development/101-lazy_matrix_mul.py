#!/usr/bin/python3
"""
	multiplies a pair of matrices using numpy
"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
        lazy_matrix_mul - multiplies two matrices

        Returns: product
    """
    first_array = np.array(m_a)
    second_array = np.array(m_b)

    return np.dot(first_array, second_array)
