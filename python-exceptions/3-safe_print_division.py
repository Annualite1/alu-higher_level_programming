#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints result safely."""
    result = None

    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
