#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in i:
            if i.index(x) == (len(i) - 1):
                print("{}".format(x))
            else:
                print("{}".format(x), end=" ")
