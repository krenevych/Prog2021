class QuadraticEquation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        print(f"{self.a}x^2 + {self.b}x + {self.c} = 0")

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solutions(self):
        if self.a == 0:  # bx + c = 0
            if self.b == 0: # c = 0
                if self.c == 0:  # 0 = 0
                    return "INF"
                else:           # 5 = 0
                    return ()
            else:
                x = -self.c / self.b
                return x,
        else:  # ax^2 + bx + c = 0
            d = self.discriminant()
            if d < 0:
                return ()  # порожній кортеж, бо розв'язків не існує
            elif d == 0:
                x = -self.b / (2.0 * self.a)
                return x,  # кортеж з одного елементу
            else:
                d2 = d ** 0.5
                x1 = (-self.b - d2) / (2.0 * self.a)
                x2 = (-self.b + d2) / (2.0 * self.a)
                return x1, x2


if __name__ == "__main__":
    # a1 = int(input("a="))
    # b2 = int(input("b="))
    # c3 = int(input("c="))
    # eq = QuadraticEquation(a1, b2, c3)
    # eq.show()
    # print(eq.solutions())

    # eq0 = QuadraticEquation(1, -4, 14)
    # eq0.show()
    # print(eq0.solutions())
    #
    # eq1 = QuadraticEquation(1, -4, 4)
    # eq1.show()
    # print(eq1.solutions())
    #
    # eq2 = QuadraticEquation(1, -3, 2)
    # eq2.show()
    # print(eq2.solutions())

    eq0 = QuadraticEquation(0, 0, 14)
    eq0.show()
    print(eq0.solutions())

    eq1 = QuadraticEquation(0, 1, 14)
    eq1.show()
    print(eq1.solutions())

    eq_inf = QuadraticEquation(0, 0, 0)
    eq_inf.show()
    print(eq_inf.solutions())
