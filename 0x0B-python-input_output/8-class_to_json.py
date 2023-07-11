#!/usr/bin/python3
"""
a module that contains a function "class_to_json"
"""


def class_to_json(obj):
    """a function that returns the dictionary description"""
    return obj.__dict__
