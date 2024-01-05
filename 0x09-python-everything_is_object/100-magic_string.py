#!/usr/bin/python3
def magic_string(iteration=[-1]):
    iteration[0] += 1
    return ("BestSchool" + (", BestSchool" * iteration[0]))
