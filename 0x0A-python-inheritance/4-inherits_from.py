#!/usr/bin/python3
"""
module that contains a function that returns True
"""


def inherits_from(obj, a_class):
    """a function that returns True if the object"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
