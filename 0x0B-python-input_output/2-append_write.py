#!/usr/bin/python3
"""Module: 2-append_write
This is a function that appends a string at the end of a text file (UTF8)
Returns the number of characters added
"""


def append_write(filename="", text=""):
    """This function appends a string to the end of a text file

    Args:
        - filename: Name of file that will want to append string to
        - text: The string to be appended to the file
    Returns the number of characters added
    """

    with open(filename, 'a+') as f:
        return f.write(text)
        
