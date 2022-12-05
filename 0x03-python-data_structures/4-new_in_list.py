#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Function that  that replaces an element in a list at
       a specific position without modifying the original list

   Args:
        my_list: list
        idx: index
        element: new element

    Returns:
        The return value: retrieves element from a list
    """
    new_list = my_list[:]
    if 0 <= idx < len(new_list):
        new_list[idx] = element
        return new_list
    return my_list
