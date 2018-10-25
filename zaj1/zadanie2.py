from cmath import sqrt


class Punkt2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

    def __str__(self):
        return str(self.__dict__)


class Punkt3D(Punkt2D):
    def __init__(self, x, y, z):
        Punkt2D.__init__(self, x, y)
        self.z = z

    def dist(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2)


a = Punkt2D(2, 5)
b = Punkt2D(5, 6)

print a.dist(b)  # 3.162278

c = Punkt3D(2, 5, 3)
d = Punkt3D(1, 2, 5)

print c.dist(d)  # 3.741657
