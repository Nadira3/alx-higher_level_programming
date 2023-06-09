#!/usr/bin/python3
if __name__ == "__main__":
    arg_list = dir(hidden_4.pyc)
    for i in arg_list:
        if (arg_list[i][0] != '_'):
            print(arg_list[i])
