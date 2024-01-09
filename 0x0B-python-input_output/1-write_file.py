#!/usr/bin/python3
"""
A module for writing to file and returning the size of content.
"""


def write_file(filename="", text=""):
    """
    File writer and counter.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
