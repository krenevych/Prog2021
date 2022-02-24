class Equation:

    INF = "inf" # нескінченна кількість розв'язків,
                # розв'язки - вся дійсна вісь

    def __init__(self, b, c):
        self._b = b
        self._c = c

    def __str__(self):
        res = f"{self._b}x + {self._c} = 0"
        return res

    def solve(self):
        if self._b != 0: # b != 0 => 1 розв'язок
            x = -self._c / self._b
            return x, # кортеж з одного елементу, що є розв'язком рівняння
        else: # b = 0, c = 0
            if self._c == 0: # 0 = 0 => нескінченна кількість розв'язків
                return Equation.INF
            else: # с != 0, 2 = 0 => розв'язків немає
                return () # порожній кортеж, бо розв'язків немає


if __name__ == '__main__':
    eq = Equation(2, 3)
    # print(eq)
    print(f"розв'язки рівняння {eq}: ", eq.solve())

    eq = Equation(0, 3)
    # print(eq)
    print(f"розв'язки рівняння {eq}: ", eq.solve())

    eq = Equation(0, 0)
    # print(eq)
    print(f"розв'язки рівняння {eq}: ", eq.solve())