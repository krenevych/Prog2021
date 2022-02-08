class QuadraticEquation:
    def __init__(self, a, b=None, c=None):
        if isinstance(a, QuadraticEquation):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = a
            self.b = b
            self.c = c

    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solutions(self):
        if self.a == 0: # bx + c = 0
            if self.b != 0:
                x = - self.c / self.b
                return x,
            else: # c = 0
                if self.c == 0:  # 0 = 0
                    return "INF"
                else:            # 5 = 0
                    return ()
        else:           # ax^2 + bx + c = 0
            d = self.discriminant()
            if d < 0:  # рівняння немає розв'язків
                return ()
            elif d == 0: # рівняння має один розв'язок
                x = -self.b / (2.0 * self.a)
                return x,
            else: # d > 0, рівняння має два розв'язки
                d2 = d ** 0.5
                x1 = (-self.b - d2) / (2.0 * self.a)
                x2 = (-self.b + d2) / (2.0 * self.a)
                return x1, x2


if __name__ == "__main__":
    # eq1 = QuadraticEquation(1, 2, 1)
    # eq1.show()
    # print(eq1.solutions())
    #
    # eq0 = QuadraticEquation(1, -3, 3)
    # eq0.show()
    # print(eq0.solutions())
    #
    # eq2 = QuadraticEquation(1, -3, 2)
    # eq2.show()
    # print(eq2.solutions())
    #
    # linear0 = QuadraticEquation(0, 0, 3)
    # linear0.show()
    # print(linear0.solutions())
    # linear1 = QuadraticEquation(0, 1, 3)
    # linear1.show()
    # print(linear1.solutions())
    # linear_inf = QuadraticEquation(0, 0, 0)
    # linear_inf.show()
    # print(linear_inf.solutions())

    eq1 = QuadraticEquation(1, 2, 1)
    eq1.show()
    print(eq1.solutions())

    eq2 = QuadraticEquation(eq1)
    eq2.a = -100
    eq2.show()
    print(eq2.solutions())


