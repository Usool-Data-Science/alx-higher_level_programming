#!/usr/bin/python3
import sys
from sys import argv

from calculator_1 import add, sub, mul, div

args = len(argv) - 1
operators = ['+', '-', '*', '/']

if __name__ == "__main__":
    a = int(argv[1])
    b = int(argv[3])
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, *, /")
        sys.exit(1)
    if argv[2] == '+':
        result = add(a, b)
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    elif argv[2] == '-':
        result = sub(a, b)
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    elif argv[2] in ['*', '\*']:
        result = mul(a, b)
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    else:
        result = div(a, b)
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
