#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer with "{:d}".format()

    Args:
        value (int): This is the integer to print.

    Return:
        If a TypeError or ValueError occurs, print False
        Else, print True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
