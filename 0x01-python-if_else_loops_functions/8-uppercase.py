#!/usr/bin/python3
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def uppercase(string):
    index = 0
    for value in string:
        if (value in lower):
            while lower[index] != value:
                index += 1
            print("{}".format(upper[index]), end="")
        else:
            print("{}".format(value), end="")
        index = 0
    else:
        print("")
