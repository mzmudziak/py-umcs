#!/usr/bin/python

import sys


def patternSearch(pattern, f):
    for line in f:
        if pattern in line:
            print line


def read():
    file_lines = ''
    while True:
        l = sys.stdin.readline()
        if l == "":
            return file_lines
        file_lines += l


if sys.argv[2] == '-':
    patternSearch(sys.argv[1], read())
else:
    with open(sys.argv[2]) as plik:
        patternSearch(sys.argv[1], plik)
