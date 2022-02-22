from Equation import Equation


class QuadraticEquation(Equation):

    def __init__(self, a, b, c):
        super().__init__(b, c)
        self._a = a

    def __str__(self):
        res = f"{self._a}x^2 + "
        res += super().__str__()
        return res

    def discriminant(self):
        return self._b ** 2 - 4 * self._a * self._c

    def solve(self):
        if self._a == 0:  # bx + c = 0
            return super().solve()
        else:  # a != 0
            d = self.discriminant()
            if d < 0:
                return ()  # порожній кортеж, бо розв'язків немає
            elif d == 0:
                x = -self._b / (2 * self._a)
                return x,  # кортеж, з одного елементу, що є розв'язоком рівняння
            else:  # d > 0
                d2 = d ** 0.5
                x1 = (-self._b - d2) / (2 * self._a)
                x2 = (-self._b + d2) / (2 * self._a)
                return x1, x2


if __name__ == '__main__':
    eq2 = QuadraticEquation(2, 8, 8)
    print(eq2)
    print(eq2.solve())

    eq2 = QuadraticEquation(1, -3, 2)
    print(eq2)
    print(eq2.solve())

    eq2 = QuadraticEquation(1, -3, 22)
    print(eq2)
    print(eq2.solve())
