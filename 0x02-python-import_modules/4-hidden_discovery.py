#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    arg_list = dir(hidden_4)
    for i in range(len(arg_list)):
        if (arg_list[i][0] != '_'):
            print(arg_list[i])
