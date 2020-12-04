#!/usr/bin/env python
"""
info about project here
"""



...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def printmatrix(lijst):
    for y in range(len(lijst)):
        print("")
        for x in range(len(lijst)):
            print(lijst[x][y], end="")

    for j in lijst: #print zoals gegeven
        for j1 in j:
            print(j1, end=" ")
        print("")


def main():
    lijst = [['.', '.', '.', '.', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['.', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.']]
    printmatrix(lijst)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
