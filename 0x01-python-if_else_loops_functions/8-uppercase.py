#!/usr/bin/python3
def uppercase(str):
    for i in str.lower():
        if 'a' <= i <= 'z':
            stru = ord(i) - 32
            print("{}".format(chr(stru)), end="")
        else:
            print("{}".format(i), end="")
        print()
