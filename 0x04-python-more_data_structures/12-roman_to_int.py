#!/usr/bin/python3
def roman_to_int(roman_string):
    num = [1, 5, 10, 50, 100, 500, 1000]
    idx = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    total = 0
    if roman_string and isinstance(roman_string, str):
        rlen = len(roman_string)
        for i in range(rlen):
            for j in range(len(idx)):
                if roman_string[i] == idx[j]:
                    value = int(num[j])
                    if i < rlen - 1 and \
                            idx.index('{}'.format(roman_string[i + 1])) > j:
                        total -= value
                    else:
                        total += value
        return total
    else:
        return 0
