#!/usr/bin/python3
"""
    A function that returns the key with the maximum integer.
"""


def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    key_main, value_main = "", 0
    for k, v in a_dictionary.items():
        if v > value_main:
            key_main, value_main = k, v
        else:
            pass
    return (key_main)
