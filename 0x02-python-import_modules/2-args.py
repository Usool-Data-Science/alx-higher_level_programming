#!/usr/bin/python3
from sys import argv
size = len(argv) - 1
if __name__ == "__main__":
    if size == 0:
        print("{} arguments.".format(size))
    elif size == 1:
        print("{} argument:".format(size))
        print("{}: {}".format(size, argv[size]))
    else:
        print("{} arguments:".format(size))
        for i in range(1, size + 1):
            print("{}: {}".format(i, argv[i]))
