class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # self.d = self.b ** 2 - 4 * self.a * self.b !!!! DO NOT DO THIS!!!

    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")

    def discriminant(self):
        d = self.b ** 2 - 4 * self.a * self.c
        return d

    def solve(self):
        if self.a == 0:  # рівняння вироджується у лінійне
            # bx + c = 0
            if self.b != 0:
                x = -self.c / self.b
                return x,
            else: # c = 0
                if self.c == 0: # 0 = 0
                    return "inf"
                else:
                    return ()
        else:
            d = self.discriminant()
            if d < 0:  # розв'язків немає
                return ()
            elif d == 0:  # один розв'язок
                x = - self.b / (2.0 * self.a)
                return x,
            else:  # два розв'язки
                d2 = d ** 0.5
                x1 = (- self.b - d2) / (2.0 * self.a)
                x2 = (- self.b + d2) / (2.0 * self.a)
                return x1, x2


if __name__ == "__main__":
    eq = QuadraticEquation(-4, 0, 10)
    eq.show()
    print(eq.solve())

    eq2 = QuadraticEquation(1, -3, 2)
    eq2.show()
    print(eq2.solve())

    eq3 = QuadraticEquation(1, 2, 1)
    eq3.show()
    print(eq3.solve())

    eq4 = QuadraticEquation(1, 2, 4)
    eq4.show()
    print(eq4.solve())

    eq5 = QuadraticEquation(0, 0, 0)
    eq5.show()
    print(eq5.solve())
