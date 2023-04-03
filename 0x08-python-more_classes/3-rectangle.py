#!/usr/bin/python3
"""3 - String representation"""


class Rectangle():
    """Representation of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation with width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public method that returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Public method that returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """__str__ method for rectangle"""
        if self.width == 0 or self.height == 0:
            return ("")
        string = ""
        for i in range(self.height):
            for j in range(self.width):
                string += '#'
            if i != self.height - 1:
                string += '\n'
        return string
