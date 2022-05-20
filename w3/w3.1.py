class Fraction:
    __slots__ = ('__numerator', '__denominator')

    def __init__(self, num: int, den: int):
        self.__numerator = num
        self.__denominator = den
