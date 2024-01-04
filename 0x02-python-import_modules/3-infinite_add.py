#!/usr/bin/python3
import sys


def addition():
    total = 0
    if len(sys.argv) == 1:
        print("{}".format(len(sys.argv) - 1))
    else:
        for i in range(1, len(sys.argv)):
            total += int(sys.argv[i])
        print("{}".format(total))


if __name__ == "__main__":
    addition()
