#!/usr/bin/python3

""" define a rectangle """


class Rectangle:
    """
    represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initialization of rectangle

        args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        return the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        seth the width of the rectangle
        """
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        return the height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height of the rectangle
        """
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
