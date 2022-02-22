class Equation:

    def __init__(self, b, c):
        self.__b = b
        self.__c = c

    def __str__(self):
        sign_c = "+" if self.__c >= 0 else "-" if self.__c < 0 else ""
        res = f"{self.__b}x {sign_c} {abs(self.__c)} = 0"
        return res

    def solve(self):
        if self.__b == 0:  # c = 0
            if self.__c == 0:  # 0 = 0
                return "inf"
            else:
                return ()
        else:  # bx + c = 0
            x = -self.__c / self.__b
            return x,


if __name__ == '__main__':
    eq = Equation(0, 0)
    print(eq)
    print(eq.solve())

    eq = Equation(0, -2)
    print(eq)
    print(eq.solve())

    eq = Equation(3, -2)
    print(eq)
    print(eq.solve())
