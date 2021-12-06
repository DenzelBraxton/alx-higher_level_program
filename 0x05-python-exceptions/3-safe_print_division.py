#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (FloatingPointError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result

safe_print_division(4, 2)
