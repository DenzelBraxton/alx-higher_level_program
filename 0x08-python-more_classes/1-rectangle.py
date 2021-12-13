#!/usr/bin/python3
"""Module 0-rectangle
The module defines an empty rectangle class"""

class Rectangle:
    """This class defines by width and height"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance and accept the following argument.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """This retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the width of a Rectangle instance

        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the height of a Rectangle instance

        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value