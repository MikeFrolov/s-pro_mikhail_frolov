class MixinFraction:
    @staticmethod
    def sub(fraction_1, fraction_2):
        num = fraction_1.get_num * fraction_2.get_den - fraction_1.get_den * fraction_2.get_num
        den = fraction_1.get_den * fraction_2.get_den
        return Fraction(num, den)

    @staticmethod
    def add(fraction_1, fraction_2):
        num = fraction_1.get_num * fraction_2.get_den + fraction_1.get_den * fraction_2.get_num
        den = fraction_1.get_den * fraction_2.get_den
        return Fraction(num, den)

    @staticmethod
    def mul(fraction_1, fraction_2):
        num = fraction_1.get_num * fraction_2.get_num
        den = fraction_1.get_den * fraction_2.get_den
        return Fraction(num, den)

    @staticmethod
    def truediv(fraction_1, fraction_2):
        num = fraction_1.get_num * fraction_2.get_den
        den = fraction_1.get_den * fraction_2.get_num
        return Fraction(num, den)


class Fraction(MixinFraction):
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

    @classmethod
    def str_fraction(cls, string: str) -> isinstance:
        num, den = [int(_.strip()) for _ in string.split('/')]
        return cls(num, den)

    def __str__(self) :
        return f'{self.get_num}/{self.get_den}'


if __name__ == "__main__":
    #  Create class instances
    fr1 = Fraction(4, 3)
    fr2 = Fraction.str_fraction("1/7")

    print("Base class methods:")
    print(f"Sub: {fr1.__sub__(fr2)}")
    print(f"Add: {fr1.__add__(fr2)}")
    print(f"Mul: {fr1.__mul__(fr2)}")
    print(f"Truediv: {fr1.__truediv__(fr2)}\n")

    print("Mixin class methods:")
    print(f"Sub: {fr1 - fr2}")
    print(f"Add: {fr1 + fr2}")
    print(f"Mul: {fr1 * fr2}")
    print(f"Truediv: {fr1 / fr2}")
