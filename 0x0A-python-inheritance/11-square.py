#!/usr/bin/python3
"""
module that contains a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
"""

Rectangle = __import__('9-rectangle').Rectangle
    
    
class Square(Rectangle):
    """a class that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py)."""
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
