#!/usr/bin/python3
"""
A module for appending a new line to a file.
"""


def append_write(filename="", text=""):
    """
    Line writer/Appender.
    It doesn't overwrite existing lines.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
