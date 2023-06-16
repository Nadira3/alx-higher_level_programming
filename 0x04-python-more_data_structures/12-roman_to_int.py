#!/usr/bin/python3
def roman_to_int(roman_string):
    num = [1, 5, 10, 50, 100, 500, 1000]
    idx = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    total = 0
    flag = 0
    if roman_string and isinstance(roman_string, str):
        for i in roman_string:
            for j in range(len(idx)):
                if i == idx[j]:
                    value = int(num[j])
                    flag = j
                    total += value
        return total
    else:
        return 0

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
