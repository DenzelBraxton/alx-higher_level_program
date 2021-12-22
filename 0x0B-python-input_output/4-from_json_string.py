#!/usr/bin/python3
"""Module: 4-from_json_string
Returns an object (Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """This is a function that returns an object represented by a JSON string
    Returns (Python data structure)

    Args:
        - my_str: the argument to be deserialized
    """
    
    return json.loads(my_str)
