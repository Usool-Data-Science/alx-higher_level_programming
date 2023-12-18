#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter, i = 0, 0
    try:
        while (i < x):
            print("{}".format(my_list[i]), end="")
            counter += 1
            i += 1
        print("")
    except IndexError as err:
        print("")
    return counter
