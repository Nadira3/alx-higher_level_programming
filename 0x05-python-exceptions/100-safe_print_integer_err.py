#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    type_list = [str, list, dict, set, tuple, float]
    try:
        print("{:d}".format(value))
        return True
    except:
        for item in range(len(type_list) - 1):
            if isinstance(value, type_list[item]):
                value_type = str(type_list[item])
                value = ""
                i = 0
                while value_type[i] != '\'':
                    i += 1
                while value_type[i] != '>':
                    value += value_type[i]
                    i += 1

        print("Exception: Unknown format code 'd' for object of type {}".format(value),file=sys.stderr)
        return False

