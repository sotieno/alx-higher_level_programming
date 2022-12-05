#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers

   Args:
        matrix: list of lists

    Returns:
        The return value: entries in the matrix
    """
    for entry in matrix:
        print(" ".join("{:d}".format(i) for i in entry))
