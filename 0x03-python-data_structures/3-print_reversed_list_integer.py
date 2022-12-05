#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list, in reverse order

    Args:
        my_list: list to be reversed

    Returns:
        The return value: elements of list printed in reverse order
    """
    if my_list:
        for num in my_list[::-1]:
            print("{:d}".format(num))
