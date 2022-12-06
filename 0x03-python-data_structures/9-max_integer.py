#!/usr/bin/python3
def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list

   Args:
        my_list: list of integers

    Returns:
        The return value: biggest integer of a list
    """
    if my_list:
        max = my_list[0]
        for num in my_list:
            if num > max:
                max = num
        return max
    return None
