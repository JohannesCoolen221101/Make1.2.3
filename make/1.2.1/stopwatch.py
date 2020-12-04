#!/usr/bin/env python
"""
info about project here
"""

import time

...

__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


def start():
    starttijd = time.time()
    print(starttijd)
    return starttijd


def stop(starttijd):
    stoptijd = time.time()
    loopduur = stoptijd - starttijd
    print("je hebt gelopen voor " + str(loopduur) + " seconden")


def main():
    input("druk enter om te starten")
    print("start")
    starttijd = start()


    input("druk enter om te stoppen")
    print("de stopwatch is gestopt")
    stop(starttijd)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
