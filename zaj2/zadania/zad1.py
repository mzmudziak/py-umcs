#!/usr/bin/python

import sys

print sys.argv[1]

plik = open(sys.argv[1])
napis = plik.read()

print napis

slownik = {}

split = napis.split('\n')
split = filter(None, split)

for x in split:
    klucz = x.split(':')[0].strip()
    wartosc = x.split(':')[1].strip()
    slownik[klucz] = wartosc

print slownik

plik.close()
