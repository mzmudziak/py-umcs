class samochod:
    kolor = None
    def setKolor(self, kolor):
        self.kolor = kolor


class osobowy(samochod):
    marka = 'mercedes'


sam = osobowy()

sam.setKolor('czerwony')
print ("To jest %s %s" % (sam.kolor, sam.marka))

