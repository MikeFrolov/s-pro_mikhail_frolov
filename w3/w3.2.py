from math import sqrt


class Point2D:
    __count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point2D.__count += 1

    def distance(self, p2):
        return sqrt(((self.x - p2.x) ** 2) + ((self.y - p2.y) ** 2))

    def get_count(self):
        return self.__count


class Point3D(Point2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z
