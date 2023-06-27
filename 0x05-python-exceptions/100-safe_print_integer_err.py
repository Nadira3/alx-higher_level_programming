#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    type_list = [int, str, list, dict, set, tuple, float]
    try:
        print("{:d}".format(value))
        return True
    except:
        for item in range(len(type_list) - 1):
            if isinstance(value, type_list[item]):
                value_type = type_list[item]
        print("Exception: Unknown format code 'd' for object of type {}".format(value_type),file=sys.stderr)
        return False
