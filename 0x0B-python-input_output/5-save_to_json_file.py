#!/usr/bin/python3
"""Module: 5-save_to_json_file
This is a function that writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation

    Args:
        - my_obj: the json object
        - filename: the name of the file
    """
    
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
