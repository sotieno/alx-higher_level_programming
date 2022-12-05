#!/usr/bin/python3
def element_at(my_list, idx):
    """Function retrieves an element from a list

    Args:
        my_list: list of integers
        idx: element index

    Returns:
        The return value: retrieves element from a list
    """
    return (my_list[idx] if 0 <= idx < len(my_list) else None)
