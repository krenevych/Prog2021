from QuadraticEquation import QuadraticEquation
from Equation import Equation


class BiQuadraticEquation(QuadraticEquation):

    def __str__(self):
        res = f"{self._a}x^4 + {self._b}x^2 + {self._c} = 0"
        return res

    def solve(self):
        solutions_quadratic = super().solve()
        if solutions_quadratic == Equation.INF:
            return Equation.INF
        else:
            solutions = set() # множина розв'язків
            for y in solutions_quadratic:
                if y < 0:
                    continue

                x1 = y ** 0.5
                x2 = -x1
                solutions.add(x1)
                solutions.add(x2)
            return tuple(solutions)





if __name__ == '__main__':
    eq = BiQuadraticEquation(0, 0, 0)
    print(f"розв'язки рівняння {eq}: ", eq.solve())

    eq = BiQuadraticEquation(1, -4, 4)
    print(f"розв'язки рівняння {eq}: ", eq.solve())

    eq = BiQuadraticEquation(1, -5, 4)
    print(f"розв'язки рівняння {eq}: ", eq.solve())

    eq = BiQuadraticEquation(1, -5, 41)
    print(f"розв'язки рівняння {eq}: ", eq.solve())

