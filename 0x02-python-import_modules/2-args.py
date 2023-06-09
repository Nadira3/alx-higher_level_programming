#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    print("{} argument{}".format(n, "s:" if n > 1 else "s." if n < 1 else ":"))
    for i in range(n):
        print("{}: {}".format(i + 1, argv[i + 1]))
