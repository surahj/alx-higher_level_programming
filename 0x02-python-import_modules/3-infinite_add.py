#!/usr/bin/python3
import sys

if __name__ == "__main__":

    result = 0
    count = len(sys.argv) - 1

    for i in range(count):
        result += int(sys.argv[i + 1])

    print("{}".format(result))
