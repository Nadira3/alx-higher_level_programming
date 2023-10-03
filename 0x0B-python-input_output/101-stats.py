#!/usr/bin/python3
""" Log parse module """


import sys

count = 0
total_size = 0
obj = {}
statusCode = ""

try:
    for line in sys.stdin:
        if count >= 10:
            count = 0
            print(f"File size: {total_size}")
            for key, value in sorted(obj.items()):
                print(f"{key}: {value}")
            total_size = 0
        statusCode = line.split()[-2]

        if statusCode in obj:
            obj[statusCode] += 1
        else:
            obj[statusCode] = 1

        count += 1
        total_size += int(line.split()[-1])
except KeyboardInterrupt:
        print(f"File Size: {total_size}")
        for key, value in sorted(obj.items()):
            print(f"{key}: {value}")
