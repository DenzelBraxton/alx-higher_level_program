#!/usr/bin/python3
"""Module: 8-class_to_json
This is a function that returns the dictionary description 
This is return with a simple data structure (list, dictionary, string, integer and boolean) for JSON
"""


def class_to_json(obj):
    """Return the sample data structure
    As list, dictionary, string, integer and boolean
    As JSON

    Args:
        - obj: The object to be open
    """

    return obj.__dict__
