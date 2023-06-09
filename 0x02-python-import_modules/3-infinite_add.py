#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    arg_sum = 0
    for i in range(n):
        arg_sum += int(argv[i + 1])
    print("{}".format(arg_sum))
