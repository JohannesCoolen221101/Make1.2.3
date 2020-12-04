#!/usr/bin/env python
"""
info about project here
"""


...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def printlijst(lijst):
    for woorden in lijst:
        print(woorden)


def main():
    lijst = ["deze", "oefening", "is", "too", "ez"]
    printlijst(lijst)



if __name__ == '__main__':  # code to execute if called from command-line
    main()
