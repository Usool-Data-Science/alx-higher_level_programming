#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    new_string = ""
    for i in range(len(str)):
        if i != n:
            new_string += str[i]
    return new_string
