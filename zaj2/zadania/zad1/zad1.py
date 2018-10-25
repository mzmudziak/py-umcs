napis = '''k1: w2
k2: w2
k3: w3'''

slownik = {

}
print napis.split('\n')

for x in napis.split('\n'):
    klucz = x.split(': ')[0]
    wartosc = x.split(': ')[1]
    slownik[klucz] = wartosc


print slownik
