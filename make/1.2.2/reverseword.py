#!/usr/bin/env python
"""
info about project here
"""


...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def reverseword(woord):
    result = []
    for i in woord:
        result.insert(0, i)
    print("".join(result))


def main():
    woord = list(input("geef een woord"))
    reverseword(woord)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
