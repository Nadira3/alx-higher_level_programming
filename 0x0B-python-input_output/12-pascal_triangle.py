#!/usr/bin/python3
"""
    pascal triangle module
"""


def pascal_triangle(n):
    """
        returns a triangle of numbers
    """
    
    result = []

    if n > 0:
        for i in range(n):
            if not i:
                result.append([i + 1])
            else:
                result.append([1])
                for j in range(len(result[i - 1])):
                    if len(result[i]) == len(result[i - 1]):
                        result[i].append(1)
                        break
                    
                    if i == 1:
                        result[i].append(1)
                        continue

                    result[i].append(result[i - 1][j] + result[i - 1][j + 1])
    
    return result
