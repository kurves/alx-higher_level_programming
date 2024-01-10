#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    doubled_dictionary = a_dictionary.copy()
    for k, v in doubled_dictionary.items():
        doubled_dictionary[k] = v * 2
    return doubled_dictionary
