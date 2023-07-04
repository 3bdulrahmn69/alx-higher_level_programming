#!/usr/bin/python3
"""
function that divides all elements of a matrix and Returns a new matrix
"""
def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        len_rows.append(len(row))
        for e in row:
            if type(e) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row_count += 1

        if len(set(len_rows)) > 1:
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) not in [int, float]:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        new_matrix = list(map(lambda row:list(map(lambda x: round(x/div, 2), row)), matrix))
        return new_matrix
