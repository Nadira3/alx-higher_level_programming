#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list_length = 0
    try:
        while list_length < x:
            print("{}".format(my_list[list_length]), end="")
            list_length += 1
        print()
    except IndexError:
        print()
    return (list_length)
