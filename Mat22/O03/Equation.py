class Equation:

    def __init__(self, b, c):
        self._b = b
        self._c = c

    def __str__(self):
        sign_c = "+" if self._c >= 0 else "-" if self._c < 0 else ""
        res = f"{self._b}x {sign_c} {abs(self._c)} = 0"
        return res

    def solve(self):
        if self._b == 0:  # c = 0
            if self._c == 0:  # 0 = 0
                return "inf"
            else:
                return ()
        else:  # bx + c = 0
            x = -self._c / self._b
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
