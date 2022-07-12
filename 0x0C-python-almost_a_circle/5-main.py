#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle
from models.base import Base

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)
    print(type(r1).__name__)

    r2 = Rectangle(5, 5, 1)
    print(r2)
