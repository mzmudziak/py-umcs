#!/usr/bin/python

import sys

print sys.argv[1]

plik = open(sys.argv[1])
napis = plik.read()

print napis

slownik = {}

splitted = napis.split('\n')
splitted = filter(None, splitted)

for x in splitted:
    klucz = x.split(': ')[0]
    wartosc = x.split(': ')[1]
    slownik[klucz] = wartosc

print slownik

plik.close()
