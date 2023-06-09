#!/usr/bin/python3
for i in range(65, 91):
    __import__("os").write(1, "{:c}".format(i).encode("UTF-8"))
