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
    return np.dot(m_a, m_b)
