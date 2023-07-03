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
        """ width geter """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TabError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height geter """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TabError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
