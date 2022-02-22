from QuadraticEquation import QuadraticEquation
from Equation import Equation


class BiQuadraticEquation(QuadraticEquation):

        def __str__(self):
            res = f"{self._a}x^4 + {self._b}x^2 + {self._c} = 0"
            return res

        def solve(self):
            eq2 = QuadraticEquation(self._a, self._b, self._c) # eq2: ay^2 + by + c = 0
            solutions_quadratic = eq2.solve()
            if solutions_quadratic == Equation.INF:
                return Equation.INF
            else:
                solutions = set()
                for y in solutions_quadratic:
                    if y < 0:
                        continue
                    elif y == 0:
                        solutions.add(0)
                    else: # y > 0
                        solutions.add(y ** 0.5)
                        solutions.add(-y ** 0.5)
                solutions = list(solutions)
                solutions.sort()
                return tuple(solutions)


if __name__ == '__main__':
    eq4 = BiQuadraticEquation(1, -8, 16)
    print(eq4)
    print(eq4.solve())

    eq4 = BiQuadraticEquation(1, -5, 4)
    print(eq4)
    print(eq4.solve())

    eq4 = BiQuadraticEquation(1, 3, -4)
    print(eq4)
    print(eq4.solve())