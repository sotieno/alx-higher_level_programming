#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Function that prints all integers in a list

    Args:
        my_list: list of integers

    Returns:
        The return value: print one integer per line
    """
    for num in my_list:
        print("{:d}".format(num))
