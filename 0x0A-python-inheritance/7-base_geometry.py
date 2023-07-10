#!/usr/bin/python3
"""
module that contains a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """ a class (based on 6-base_geometry.py)."""
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
