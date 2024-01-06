#!/usr/bin/python3
import sys
import calculator_1


def calculator():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if sys.argv[2] == "+":
            result = calculator_1.add(int(sys.argv[1]), int(sys.argv[3]))
            print("{} + {} = {}".format(sys.argv[1], sys.argv[3], result))
        elif sys.argv[2] == "-":
            result = calculator_1.sub(int(sys.argv[1]), int(sys.argv[3]))
            print("{} - {} = {}".format(sys.argv[1], sys.argv[3], result))
        elif sys.argv[2] == "*":
            result = calculator_1.mul(int(sys.argv[1]), int(sys.argv[3]))
            print("{} * {} = {}".format(sys.argv[1], sys.argv[3], result))
        elif sys.argv[2] == "/":
            result = calculator_1.div(int(sys.argv[1]), int(sys.argv[3]))
            print("{} / {} = {}".format(sys.argv[1], sys.argv[3], result))


if __name__ == "__main__":
    calculator()
