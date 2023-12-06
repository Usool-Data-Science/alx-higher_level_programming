#!/usr/bin/python3
"""
    A function that find the integer equivalence
    of roman numerals.
"""


def roman_to_int(roman_string):
    roman_dict = dict(
            I=1, II=2, III=3, IV=4, V=5,
            VI=6, VII=7, VIII=8, IX=9, X=10,
            L=50, C=100, D=500, M=1000)
    result = 0
    if roman_string in list(roman_dict):
        result += roman_dict[roman_string]
    else:
        for num in roman_string:
            result += roman_dict[num]
    return (result)
