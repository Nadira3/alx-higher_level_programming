#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        top = i
        if not top:
            print()
        for j in top:
            print("{:d}".format(j), end=" " if j != top[-1] else '\n')
