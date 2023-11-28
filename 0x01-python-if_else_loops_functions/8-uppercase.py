#!/usr/bin/python3
lower = "abcdefghijklmnopqrstuvwxyz"


def uppercase(string):
    length = 1
    result = ''
    for value in string:
        if value in lower:
            result += chr(ord(value) - 32)
        else:
            result += value
    print("{}".format(result))
