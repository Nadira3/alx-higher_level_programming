#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if (a < b):
        for i in range(4, 6):
            c = add(a, b)
    else:
        c = add(a, b)
dis.dis(magic_calculation)
