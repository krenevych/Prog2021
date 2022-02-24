from Equation import Equation


class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__(b, c)
        self._a = a

    def __str__(self):
        quad = f"{self._a}x^2 + "
        liner = super().__str__()
        return quad + liner

    def discriminant(self):
        return self._b ** 2 - 4 * self._a * self._c

    def solve(self):
        if self._a == 0:  # bx + c = 0 - Equation
            return super().solve()
        else:             # ax^2 + bx + c = 0
            d = self.discriminant()
            if d < 0: # розв'язків немає
                return ()  # порожній кортеж, бо розв'язків немає
            elif d == 0: # один роз'язок
                x = -self._b / (2 * self._a)
                return x, # кортеж з одного елементу, що є розв'язком рівняння
            else: # d > 0, два розв'язки
                d2 = d ** 0.5 # корінь з дискримінанту
                x1 = (-self._b - d2)/ (2 * self._a)
                x2 = (-self._b + d2)/ (2 * self._a)
                return x1, x2



if __name__ == '__main__':
    eq = QuadraticEquation(1, -4, 4)
    print(f"розв'язки рівняння {eq}: ", eq.solve())

    eq = QuadraticEquation(1, -5, 4)
    print(f"розв'язки рівняння {eq}: ", eq.solve())

    eq = QuadraticEquation(1, -5, 41)
    print(f"розв'язки рівняння {eq}: ", eq.solve())
