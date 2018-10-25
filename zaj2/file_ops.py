f = open('file')

print(f.read())

for line in f:
    print line

f.close()

with open('file') as f:
    print f.read()
