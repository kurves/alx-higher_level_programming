#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        sorted_dict = sorted(a_dictionary)
        for key in sorted_dict:
            print("{}: {}".format(key, a_dictionary[key]))