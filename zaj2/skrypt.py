#!/usr/bin/env python
dictionary = {
    'k1': 'w1',
    2: '512',
    (3, 2, 1): '1321'
}
print dictionary

# print dictionary.non_existent # throws err
print dictionary.get('non_existent')  # prints None
print dictionary.get('non_existent', 'default_value')  # prints default_value

print "iterating..."
for x in dictionary.items():
    print x

print "iterating over keys.."

for x in dictionary.keys():
    print x

lista = ['a', 'b', 'c', 'd', 'e']

napis = ''

for x in lista:
    napis += x
    print napis
