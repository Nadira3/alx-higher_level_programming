#!/usr/bin/python3

def weight_average(my_list=[]):
    total = 0
    num = 0
    if my_list:
        for arg in my_list:
            product = arg[0] * arg[1]
            total += product
            num += arg[1]
    return total / num if my_list else 0

list = []
result = weight_average(list)
print("Av: {:0.2f}".format(result))
