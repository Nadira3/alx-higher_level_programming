#!/usr/bin/python3

def weight_average(my_list=[]):
    total = 0
    num = 0
    if len(my_list) > 0:
        for arg in my_list:
            product = arg[0] * arg[1]
            total += product
            num += arg[1]
    return total / num
