class Kolo(object):
    __wielksosc = None
    __felga = None

    def __init__(self, w, f):
        self.__wielksosc = w
        self.__felga = f

    def krecSie(self):
        print "Kolo o wielkosci %s i feldze %s " % (self.__wielksosc, self.__felga)

    def stoj(self):
        print "STOP!"


class Silnik(object):
    __objetosc = None
    __moc = None

    def __init__(self, objetosc, moc):
        self.__objetosc = objetosc
        self.__moc = moc

    def uruchom(self):
        print "Uruchamiam silnik o objetosci %s i mocy %s " % (self.__objetosc, self.__moc)

    def dodajGazu(self, ilosc):
        print "Dodaje %s gazu " % ilosc


class Kierownica(object):
    __model = None
    __wersja = None

    def __init__(self, model, wersja):
        self.__model = model
        self.__wersja = wersja

    def kieruj(self):
        print "Kieruje kierownica %s o wersji %s" % (self.__model, self.__wersja)

    def skrecaj(self, kierunek):
        print "Skrecam w %s" % kierunek


class Samochod(Kolo, Kierownica, Silnik):
    __marka = None
    __rokProdukcji = None

    def __init__(self, marka, rokProdukcji, model, wersja, objetosc, moc, wielkosc, felga):
        Silnik.__init__(self, objetosc, moc)
        Kierownica.__init__(self, model, wersja)
        Kolo.__init__(self, wielkosc, felga)
        self.__marka = marka
        self.__rokProdukcji = rokProdukcji

    def start(self):
        self.uruchom()
        self.dodajGazu(5)
        self.krecSie()

    def skret(self, kierunek):
        self.kieruj()
        self.skrecaj(kierunek)

    def stop(self):
        self.stoj()


samochod = Samochod("Fiat", "15", "Punto", "51", "250", "15", "16", "13")

samochod.start()
samochod.skret("lewo")
samochod.stop()
