#!/usr/bin/python3
def uppercase(str):
    n = len(str)
    for i in range(n):
        p = ord(str[i])
        if p >= 97 and p <= 122:
            p -= 32
            print("{:c}".format(p) if i < n - 1 else "{:c}\n".format(p), end="")
        else:
            print("{:c}".format(p) if i < n - 1 else "{:c}\n".format(p), end="")
