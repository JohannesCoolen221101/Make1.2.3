#!/usr/bin/env python
"""
info about project here
"""


...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"
def telenprintlijst(lijst):
    x = 0
    for woorden in lijst:
        print(woorden)
        x += 1

    return x


def main():
    lijst = ["deze", "oefening", "is", "too", "ez"]
    x = telenprintlijst(lijst)
    print(x)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
