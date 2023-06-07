#!/usr/bin/python3
for i in range(1, 100):
    if i > int((str(i))[::-1]):
        continue
    if i > 9:
        if str(i)[0] == str(i)[1]:
            continue
    print("{:02d}".format(i) if i < 10 else "{:d}".format(i), end="")
    print(", " if i < 89 else '\n', end="")
