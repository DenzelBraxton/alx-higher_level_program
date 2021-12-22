#!/usr/bin/python3
"""Module: 1-write_file
This is a function that writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """This function writes a string to a text file
    Args:
        - filename: the name of the file that is to be write to
        - text: the string to be added to the file
    """

    with open(filename, 'w+') as f:
        return f.write(text)
