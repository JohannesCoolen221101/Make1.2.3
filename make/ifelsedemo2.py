#!/usr/bin/env python
"""
info about project here
"""



...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():
    x = input("geef een getal ")
    x = int(x)
    if (x % 2) == 0:
        print("even")
    else:
        print("oneven")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
