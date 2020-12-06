#!/usr/bin/env python
"""
info about project here
"""


__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


class liedje:
    def __init__(self,tekst):    # initialiseer de classe met een tekst
        self.tekst = tekst

    def zingen(self):
        for woord in self.tekst:  # lees elk woord af op een apparte lijn
            print(woord)




def main():
    tekst = ["Happy", "Birthday", "to", "You", "Happy", "Birthday", "to", "You", "Happy", "Birthday", "Dear", "(name)", "Happy", "Birthday", "to", "You."]
    happy_birthday = liedje(tekst)
    happy_birthday.zingen()


if __name__ == '__main__':  # code to execute if called from command-line
    main()
