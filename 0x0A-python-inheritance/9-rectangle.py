#!/usr/bin/python3
"""
module that contains a class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class that inherits from BaseGeometry (7-base_geometry.py)"""
    def __init__(self, width, height):
        """Instantiation"""
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area method implemented"""
        return self.__height * self.__width

    def __str__(self):
        """rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
