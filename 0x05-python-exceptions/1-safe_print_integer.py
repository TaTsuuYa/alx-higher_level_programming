#!/usr/bin/python3


def safe_print_integer(value):
    if value == None:
        return False

    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    else:
        return True
