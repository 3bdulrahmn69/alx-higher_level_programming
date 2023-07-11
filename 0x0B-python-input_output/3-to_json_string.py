#!/usr/bin/python3
"""
a module that contains a function "to_json_string"
"""

import json


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object"""
    return json.dumps(my_obj)
