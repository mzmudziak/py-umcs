class A(object):
    def __init__(self, zmienna):
        self.zmienna = zmienna

    def __add__(self, other):
        return self.zmienna + other.zmienna


a = A(1)
b = A(2)


print a + b


class Czlowiek(object):
    def __init__(self, login, name, surname):
        self.login = login
        self.name = name
        self.surname = surname


dominik = Czlowiek("wesivin", "Dominik", "Zmudziak")
weronika = Czlowiek("modzi", "Weronika", "Modzelewska")


print dominik + weronika
