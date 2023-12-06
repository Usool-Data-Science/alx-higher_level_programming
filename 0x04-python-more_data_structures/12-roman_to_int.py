#!/usr/bin/python3
"""
    A function that find the integer equivalence
    of roman numerals.
"""


def roman_to_int(roman_string):
    roman_dict = {
            'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
            'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result, previous_result = 0, 0
    if not roman_string or not isinstance(roman_string, str):
        return (result)

    for i in reversed(roman_string):
        value = roman_dict.get(i, 0)
        if value < previous_result:
            result -= value
        else:
            result += value
        previous_result = value
    return (result)
