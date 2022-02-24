from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

if __name__ == '__main__':

    equations = []

    with open("input01.txt") as f:
        for line in f:
            coef = [float(el) for el in line.split()]
            # print(coef)
            coef_num = len(coef)
            if coef_num == 2:  # лінійне рівняння
                eq = Equation(*coef)
                equations.append(eq)
            elif coef_num == 3:  # квадратне рівняння
                eq = QuadraticEquation(*coef)
                equations.append(eq)
            elif coef_num == 5:  # біквадратне рівняння
                eq = BiQuadraticEquation(coef[0], coef[2], coef[4])
                equations.append(eq)

    # for eq in equations:
    #     print(f"розв'язки рівняння {eq}: ", eq.solve())

    equations_0 = []  # не мають розв’язків;
    equations_1 = []  # мають один розв’язок;
    equations_2 = []  # мають два розв’язки;
    equations_3 = []  # мають три розв’язки;
    equations_4 = []  # мають чотири розв’язки;
    equations_inf = []  # мають нескінченну кількість розв’язків.

    for eq in equations:
        solution = eq.solve()
        if solution == Equation.INF:
            equations_inf.append(eq)
        else:
            sol_num = len(solution)
            if sol_num == 0:
                equations_0.append(eq)
            elif sol_num == 1:
                equations_1.append(eq)
            elif sol_num == 2:
                equations_2.append(eq)
            elif sol_num == 3:
                equations_3.append(eq)
            elif sol_num == 4:
                equations_4.append(eq)

    print("\n\nне мають розв’язків")
    for e in equations_0:
        print(f"розв'язки рівняння {e}: ", e.solve())

    print("\n\nмають один розв’язок")
    for e in equations_1:
        print(f"розв'язки рівняння {e}: ", e.solve())

    print("\n\nмають два розв’язки")
    for e in equations_2:
        print(f"розв'язки рівняння {e}: ", e.solve())

    print("\n\nмають три розв’язки")
    for e in equations_3:
        print(f"розв'язки рівняння {e}: ", e.solve())

    print("\n\nмають чотири розв’язки")
    for e in equations_4:
        print(f"розв'язки рівняння {e}: ", e.solve())

    print("\n\nмають нескінченну кількість розв’язків")
    for e in equations_inf:
        print(f"розв'язки рівняння {e}: ", e.solve())
