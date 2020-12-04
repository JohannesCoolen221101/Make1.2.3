#!/usr/bin/env python
"""
info about project here
"""



...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():
    x = 0
    total = 0
    while x <= 100:
        total += x
        print(x)
        x += 1
    print(total)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
