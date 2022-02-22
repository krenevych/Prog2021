from QuadraticEquation import QuadraticEquation
from Equation import Equation


class BiQuadraticEquation(QuadraticEquation):

    def __str__(self):
        return f"{self._a}x^4 + {self._b}x^2 + {self._c} = 0"

    def solve(self):
        solutions_quadratic = super().solve()
        if solutions_quadratic == Equation.INF:
            return solutions_quadratic
        else:
            solutions = set()
            for sol_quad in solutions_quadratic:
                if sol_quad == 0:
                    solutions.add(0)
                elif sol_quad > 0:
                    x = sol_quad ** 0.5
                    solutions.add(x)
                    solutions.add(-x)

            # solutions = list(solutions)
            # solutions.sort()
            return tuple(solutions)


if __name__ == '__main__':
    eq4 = BiQuadraticEquation(0, 0, 0)
    print(eq4)
    print(eq4.solve())

    eq4 = BiQuadraticEquation(1, -5, 4)
    print(eq4)
    print(eq4.solve())

    eq4 = BiQuadraticEquation(1, -4, 0)
    print(eq4)
    print(eq4.solve())
