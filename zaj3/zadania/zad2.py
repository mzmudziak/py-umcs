f = open('file')
width = int(raw_input('Width? '))

for line in f:
    print(line[:width].center(15))


