#!/usr/bin/python3
"""Module: 0-read_file
This is a function that reads a text file (UTF8) and prints it to stdout
"""
def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Args:
        - filename: this is the file to be read
    """   

    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
