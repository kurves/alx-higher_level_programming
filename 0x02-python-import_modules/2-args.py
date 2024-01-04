#!/usr/bin/python3
import sys


def arguments():
    if len(sys.argv) == 1:
        print("{} arguments".format(len(sys.argv) - 1))
    else:
        if len(sys.argv) - 1 == 1:
            print("{} argument:".format(len(sys.argv) - 1))
            for i in range(1, len(sys.argv)):
                print("{}: {}".format(i, sys.argv[i]))
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
            for i in range(1, len(sys.argv)):
                print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    arguments()
