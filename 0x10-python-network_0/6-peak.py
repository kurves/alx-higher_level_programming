#!/usr/bin/python3
"""Funtion to find peak in a list of integes"""


def find_peak(list_of_integers):
    """peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    start = 0
    list_len= len(list_of_integers)
    mid = ((list_len - start) // 2) + start
    mid = int(mid)
    if list_len == 1:
        return list_of_integers[0]
    if list_len == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
