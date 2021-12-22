#!/usr/bin/python3
"""Module: 6-load_from_json_file.py
This is a function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """Creates an object from a "JSON file"

    Args:
        - filename: The name of the file to create ann object with
    """
    
    with open(filename, 'r') as f:
        return json.load(f)
