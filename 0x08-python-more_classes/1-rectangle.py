#!/usr/bin/python3
"""
an module that have an class -Rectangle- that defines a rectangle
"""


class Rectangle:
    """ a class that defines a rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width
    
    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height
    
    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    
    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
