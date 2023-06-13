#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        new_list = [False if i % 2 else True for i in my_list]
    return (new_list)
