from QuadraticEquation import QuadraticEquation


class BiQuadraticEquation(QuadraticEquation):

    def __str__(self):
        return f"{self._a}x^4 + {self._b}x^2 + {self._c} = 0"

    

if __name__ == '__main__':
    eq4 = BiQuadraticEquation(2, 8, 8)
    print(eq4)
