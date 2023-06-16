#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        num = []
        for x, y in a_dictionary.items():
            num.append(y)
        for x, y in a_dictionary.items():
            if y == max(num):
                return ("{:s}".format(x))
    return None
