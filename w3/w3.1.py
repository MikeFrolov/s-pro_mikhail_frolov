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
