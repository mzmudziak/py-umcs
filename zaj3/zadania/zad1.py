f = open('file')
width = raw_input('Width? ')

for line in f:
    print(line[:int(width)])


