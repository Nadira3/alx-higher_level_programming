#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for i, j in sorted(a_dictionary.items()):
            print("{:s}: {}".format(i, j))
#a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
#print_sorted_dictionary(a_dictionary)
