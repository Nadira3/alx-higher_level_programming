#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            temp = my_list[i + 1]
            my_list[i + 1] = my_list[i]
            my_list[i] = temp
    maxi = my_list[len(my_list) - 1] if len(my_list) > 0 else None
    return ("{}".format(maxi))