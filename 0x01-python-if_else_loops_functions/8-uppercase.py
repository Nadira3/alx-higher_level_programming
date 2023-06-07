#!/usr/strin/python3
def uppercase(str):
    n = len(str)
    for i in range(n):
        p = ord(str[i])
        if p >= 97 and p <= 122:
            print(f"{p - 32:c}" if i < n - 1 else f"{p - 32:c}\n", end="")
        else:
            print(f"{p:c}" if i < n - 1 else f"{p:c}\n", end="")
