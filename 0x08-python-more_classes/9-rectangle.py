#!/usr/bin/python3

""" define a rectangle """


class Rectangle:
    """
    represent a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialization of rectangle

        args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        type(self).number_of_instances += 1
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

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """
        return string representation of an object
        """
        result = "Rectangle(" + str(self.__width)
        result += ", " + str(self.__height) + ")"
        return result

    def __del__(self):
        """
        print a message when an instance is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        return the biggest rectangle base on Area

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() >= rect_2.area()):
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Class method that defines a square
        Attributes:
            cls : The parameter that points to the class
            size (int): The size of the square
        Returns:
            width = height = size
        """
        return cls(size, size)
