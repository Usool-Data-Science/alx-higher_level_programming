#!/usr/bin/python3
"""
A module for reading simple files
"""


def read_file(filename=""):
    """
    A simple file reader.
    """
    with open(filename, mode='r', encoding='utf-8') as files:
        for line in files:
            print(line, end='')
