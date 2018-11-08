#!/usr/bin/python

import difflib
import sys

first_file = sys.argv[1]
second_file = sys.argv[2]
third_file = sys.argv[3]

one = open(first_file).readlines()
two = open(second_file).readlines()
three = open(third_file, 'a')

for line in difflib.unified_diff(one, two, fromfile='file1', tofile='file2', lineterm=''):
    print line
