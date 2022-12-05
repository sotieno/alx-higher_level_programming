#!/usr/bin/python3
def no_c(my_string):
    """Function that removes all characters c and C from a string

   Args:
        my_string: string

    Returns:
        The return value: string without C or c
    """
    new_string = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch
    return new_string
