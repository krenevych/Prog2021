import cmath

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __int__(self):
        return int(self.x)

    def __bool__(self):
        return self.x != 0 and self.y != 0

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __complex__(self):
        return complex(self.x, self.y)

v = Vector2D(1, 1)

print(complex(v))

z1 = complex(3, 4)
zv = complex(v)
z2 = z1 + zv
print(z2)

print(zv ** 0.5)

# if v:
#     print(v)