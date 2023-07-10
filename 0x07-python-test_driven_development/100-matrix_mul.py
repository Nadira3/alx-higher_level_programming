#!/usr/bin/python3
"""
    main function to test matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """
        matrix_mul - multiplies two matrices

        Returns: product
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if any(not isinstance(li, list) for li in m_a):
        raise TypeError("m_a must be a list of lists")

    if any(not isinstance(li, list) for li in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(li) == 0 for li in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or any(len(li) == 0 for li in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(var, (int, float)) for li in m_a for var in li):
        raise TypeError("m_a should contain only integers or floats")

    if any(not isinstance(var, (int, float)) for li in m_b for var in li):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(m_a[0]) != len(li) for li in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if any(len(m_b[0]) != len(li) for li in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    i = 0
    result = []
    for _ in m_a:
        ans = []
        v = 0
        x = 0
        while v < len(m_b[0]):
            n = 0
            k = 0
            j = 0
            while j < len(m_b):
                n += m_b[k][x] * m_a[i][j]
                k += 1
                j += 1
            ans.append(n)
            x += 1
            v += 1
        i += 1
        result.append(ans)
    return result
