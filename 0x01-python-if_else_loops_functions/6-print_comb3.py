#!/usr/bin/python3
for i in range(100):
    if i > int((str(i))[::-1])
        continue
    print("{:02d}".format(i) if i < 10 else "{:d}".format(i), end="")
    print(", " if i < 99 else '\n', end="")
