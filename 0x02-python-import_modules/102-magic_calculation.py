#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if (a < b):
        c = add(a, b)
    else:
        c = sub(a, b)


for i in range(4, 6):
    return (add(c, i))
    c = 4
dis.dis(magic_calculation)
