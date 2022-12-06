#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Function that deletes an item at a specific position

   Args:
        my_list: list of integers
        idx: index

    Returns:
        The return value: biggest integer of a list
    """
    new_list = []
    if my_list:
        if 0 <= idx < len(my_list):
            del my_list[idx]
    return my_list
