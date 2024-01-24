#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
    except (TypeError, ValueError):
        print("Inside result: invalid input, both values must be integers")
    finally:
        if result is not None:
            print("Inside result: {:.1f}".format(result))
        return result
