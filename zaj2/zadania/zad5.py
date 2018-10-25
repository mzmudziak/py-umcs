#!/usr/bin/python

import sys


first_file = sys.argv[1]
second_file = sys.argv[2]

print first_file
print second_file

with open(first_file) as plik:
    print plik
    second = open(second_file, 'a')
    for line in plik:
        cezar = ''
        for c in line:
            cezar += chr(ord(c) + 1)
        second.write(cezar + '\n')
    second.close()
