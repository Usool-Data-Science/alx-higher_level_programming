#!/usr/bin/python3
from sys import argv

from decimal import Decimal, getcontext

getcontext().prec = 999
size = len(argv)
total = 0
if __name__ == "__main__":
    for i in range(1, size):
        total += Decimal(argv[i])
    print("{}".format(total))
