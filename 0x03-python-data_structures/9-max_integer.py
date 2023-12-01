#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    for i in my_list:
        if maximum < i:
            maximum = i
    return (maximum)
