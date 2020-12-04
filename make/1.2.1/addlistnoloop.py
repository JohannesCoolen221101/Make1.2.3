#!/usr/bin/env python
"""
info about project here
"""



...


__author__ = "Johannes Coolen"
__email__ = "johannes.coolen@student.kdg.be"
__status__ = "development"


lijst = ["dit"]
lijst.append("is")
lijst.append("een")
lijst.append("lijst")
print(lijst)


def voegtoe():
    try:
        lijst.append(input("wat wil je toevoegen "))
        nog = input("wil je nog een (y/n) ")
        print(lijst)
        if nog == "y":
            voegtoe()


def main():
    voegtoe()


if __name__ == '__main__':  # code to execute if called from command-line
    main()
