#!/usr/bin/env python
"""
info about project here
"""
import random


__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"

list = ["dit", "is", "een", "lijst"]


def randomise(lijst):
    return random.randint(0, len(lijst)-1)


def raad(string, lijst, getal):

    if string == lijst[getal]:
        print("juist")
        return True
    else:
        print("fout probeer opnieuw")
        return False


def main():
    getal = randomise(list)
    correct = False
    while correct != True:
        try:
            correct = raad(input("raad het woord je kan kiezen uit dit is een lijst"),list,getal)
        except Exception as e:
            print(e)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
