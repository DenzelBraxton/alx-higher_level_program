#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError
    except TypeError as te:
        print("Exception raised {}".format(te))