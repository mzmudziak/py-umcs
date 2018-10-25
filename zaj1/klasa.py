class klasa:
    atr1 = None
    __atr2 = None

    def setAtr2(self, zmienna):
        self.__atr2 = zmienna

    def setAtr3(self, zmienna):
        self.atr3 = zmienna

    def add(self):
        return self.atr1 + self.__atr2 + self.atr3

obiekt = klasa()
obiekt.atr1 = 4
obiekt.setAtr2(5)
obiekt.setAtr3(6)

print obiekt

