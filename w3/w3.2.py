from math import hypot


class Point2D:
    __count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D.__count += 1

    def distance(self, p2):
        return hypot(p2.x - self.x, p2.y - self.y)

    @property
    def get_count(self):
        return self.__count
