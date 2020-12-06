#!/usr/bin/env python
"""
info about project here
"""


__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def main():
    stop = ""
    lijst = []
    while stop != "s":
        lijst.append(int(input("geef de sensor waarde")))   # voeg de ingegeven waarde toe aan de lijst
        stop = input("druk op s als je wil stoppen")
    gemiddelde = str(sum(lijst)/len(lijst))                 # bereken het gemiddelde van de lijst
    print("het gemiddelde is: "+gemiddelde)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
