#!/usr/bin/python3
def uppercase(str):
    n = len(str)
    for i in range(n if n > 0 else 1):
        p = ord(str[i]) - 32 if 97 <= ord(str[i]) <= 122 else ord(str[i])
        end = "\n" if i == n - 1 else ""
        print("{:c}".format(p), end=end)
