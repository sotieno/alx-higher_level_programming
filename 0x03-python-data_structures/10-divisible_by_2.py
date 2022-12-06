#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Function that finds all multiples of 2

   Args:
        my_list: list of integers

    Returns:
        The return value: biggest integer of a list
    """
    new_list = []
    if my_list:
        for num in my_list:
            new_list.append(False if num % 2 else True)
    return new_list
