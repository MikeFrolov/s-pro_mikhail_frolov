from math import hypot


class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return hypot(p2.x - self.x, p2.y - self.y)
