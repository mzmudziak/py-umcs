class LiczbaZespolona(object):
    def __init__(self, r, i=0):
        self.r = r
        self.i = i

    def __add__(self, other):
        return LiczbaZespolona(
            self.r + other.r,
            self.i + other.i
        )

    def __sub__(self, other):
        return LiczbaZespolona(
            self.r - other.r,
            self.i - other.i
        )

    def __mul__(self, other):
        return LiczbaZespolona(
            self.r * other.r - self.i * other.i,
            self.i * other.r + self.r * other.i
        )

    def __div__(self, other):
        r = float(other.r ** 2 + other.i ** 2)
        return LiczbaZespolona(
            (self.r * other.r + self.i * other.i) / r,
            (self.i * other.r - self.r * other.i) / r
        )

    def __str__(self):
        return str(self.__dict__)


a = LiczbaZespolona(5, 4)
b = LiczbaZespolona(11, 5)

print a + b  # 16, 9
print a - b  # -6, -1
print a * b  # 35, 69
print a / b  # 0.5137, 0.1301
