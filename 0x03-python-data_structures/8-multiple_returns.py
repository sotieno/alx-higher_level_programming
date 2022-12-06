#!/usr/bin/python3
def multiple_returns(sentence):
    """Function that returns a tuple with the
    length of a string and its first character

   Args:
        sentence

    Returns:
        The return value: length of string
    """
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
