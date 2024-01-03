#!/usr/bin/python3
def uppercase(str):
    for i in str.lower():
        stru = ord(i) - 32
        print("{}".format(chr(stru) if 'a' <= i <= 'z' else i), end="")
    print()
