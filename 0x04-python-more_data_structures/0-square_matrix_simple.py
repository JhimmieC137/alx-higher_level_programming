#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_list = matrix[:]
    return [list(map(lambda x: x**2, y)) for y in copy_list]
