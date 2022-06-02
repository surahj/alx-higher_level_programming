#!/usr/bin/python3
import sys

if __name__ == "__main__":
    lenght = len(sys.argv)

    if lenght < 2:
        print("0 argumenst.")

    elif lenght == 2:
        print("{} argument:".format(lenght - 1))

    else:
        print("{} arguments:".format(lenght - 1))

        for i in range(1, lenght):
            print("{}: {}".format(i, sys.argv[i]))
