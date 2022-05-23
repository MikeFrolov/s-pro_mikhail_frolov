class Fraction:
    __slots__ = ('__numerator', '__denominator')

    def __init__(self, num: int, den: int):
        self.__numerator = num
        self.__denominator = den

    @property
    def get_num(self):
        return self.__numerator

    @property
    def get_den(self):
        return self.__denominator

    def __sub__(self, other):
        new_num = self.get_num * other.get_den - self.get_den * other.get_num
        new_den = self.get_den * other.get_den

        return Fraction(new_num, new_den)

    def __add__(self, other):
        new_num = self.get_num * other.get_den + self.get_den * other.get_num
        new_den = self.get_den * other.get_den

        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.get_num * other.get_num
        new_den = self.get_den * other.get_den

        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.get_num * other.get_den
        new_den = self.get_den * other.get_num

        return Fraction(new_num, new_den)
