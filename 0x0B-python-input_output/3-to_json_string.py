#!/usr/bin/python3
"""Module: 3-to_json_string
Returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """This function returns the JSON representation of an object (string)

    Args:
        - my_object: this is the object to be serialized (converted to json data)
    """
    return json.dumps(my_obj)
