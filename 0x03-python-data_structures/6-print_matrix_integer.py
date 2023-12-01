#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    if matrix == []:
        print("{}".format(""))
    for row in matrix:
        for column in row:
            print("{}".format(column), end=" ")
        print("{}".format(""))
