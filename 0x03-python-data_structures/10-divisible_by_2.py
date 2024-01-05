#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    doubled = []
    for num in my_list:
        if num % 2 == 0:
            doubled.append(True)
    else:
        doubled.append(False)
    return doubled
