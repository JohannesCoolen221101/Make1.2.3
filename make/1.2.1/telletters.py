#!/usr/bin/env python
"""
info about project here
"""



...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def telletters(woord):
    print(len(woord))  # len geeft de lengte van een woord terug


def main():
    telletters(input("geef een woord"))


if __name__ == '__main__':  # code to execute if called from command-line
    main()
