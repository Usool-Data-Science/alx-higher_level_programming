#!/usr/bin/python3
"""
A module for printing extra line
Accepts only strings
And print the modified string.
"""


def text_indentation(text):
    """
    Modify a string and print it out
    """
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    result = ""
    for i in text:
        if i in ['.', '?', ':']:
            result += (i + "\n\n").strip(" ")
        else:
            result += i
    print(result.strip(" "), end='')
