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

    def distance(self, p2) :
        return sqrt(((self.x - p2.x) ** 2) + ((self.y - p2.y) ** 2) + (self.z - p2.z) ** 2)


if __name__ == "__main__":
    # Create 2 instances of the Point2D class, calculate the distance between these points
    poi1 = Point2D(3, 7)
    poi2 = Point2D(-5, -9)
    print(f"Created {poi2.get_count()} instances")

    print(poi1.distance(poi2))

    # Create 2 instances of the Point3D class, calculate the distance between these points
    poi3d1 = Point3D(3, 7, 1)
    poi3d2 = Point3D(-5, -9)
    print(f"Created {poi3d2.get_count()} instances")

    print(poi3d1.distance(poi3d2))
