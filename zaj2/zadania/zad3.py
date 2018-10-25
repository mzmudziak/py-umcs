#!/usr/bin/python

import sys
from collections import Counter

print sys.argv[1]

plik = open(sys.argv[1])

napis = plik.read()
napis = napis.replace('\n', ' ')
napis = napis.strip()

slowa = napis.split(' ')
counter = Counter()

slownik = {}

print slowa
for slowo in slowa:
    counter[slowo] += 1


print dict(counter)
plik.close()
