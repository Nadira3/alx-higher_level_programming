#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        end = " "
        if i % 3 == 0:
            print("Fizz" if i % 5 != 0 else "FizzBuzz", end=end)
        elif i % 5 == 0:
            print("Buzz", end=end)
        else:
            print("{:d}".format(i), end=end)
