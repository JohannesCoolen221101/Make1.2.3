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
    tzal_al_eens_wel_zijn = ""
    while tzal_al_eens_wel_zijn == "":
        try:

            total += x
            print(x)
            x += 1
            tzal_al_eens_wel_zijn = input("zijt ge nu eindelijk al klaar \n enkel antwoorden als ik moet stoppen")
        except:
            print("sorry de input is niet correct")

    print(total)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
