#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Function replaces an element of a list at a specific position

    Args:
        my_list: list
        idx: index
        element: new element

    Returns:
        The return value: retrieves element from a list
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
