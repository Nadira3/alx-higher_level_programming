#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_len = len(str(number))
last = int(str(number)[num_len - 1])
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
else:
    print(f"Last digit of {number} is {last} and is less than 6 and is not 0")
