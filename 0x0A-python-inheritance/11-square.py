#!/usr/bin/python3
"""
module that contains a class Square that inherits from Rectangle
"""

class BaseGeometry:
    """ a class"""
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """a class that inherits from BaseGeometry"""
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


class Square(Rectangle):
    """a class that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area method implemented"""
        return self.__size * self.__size

    def __str__(self):
        """square  description"""
        return f"[square] {self.__size}/{self.__size}"
