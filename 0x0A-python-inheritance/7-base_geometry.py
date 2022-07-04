#!/usr/bin/python3
""" Defines a geometry """


class BaseGeometry:
    """ Base geometry function
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        it validate value
        args:
            name (string)
            value (int)

        """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
