class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def abs2(self):
        return self.x ** 2 + self.y ** 2

    def abs(self):
        return self.abs2() ** 0.5

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def abs2(self):
    #     return self.x ** 2 + self.y ** 2 + self.z ** 2
        # return Point2D.abs2(self) + self.z ** 2
        return super().abs2() + self.z ** 2

if __name__ == "__main__":
    a = Point2D(3, 4)
    print(f"довжина радіус вектора точки ({a.x}, {a.y}) є {a.abs()}")

    b = Point3D(3, 4, 5)
    print(f"довжина радіус вектора точки ({b.x}, {b.y}, {b.z}) є {b.abs()}")
