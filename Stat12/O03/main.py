from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

if __name__ == '__main__':

    equations = []
    with open("input03.txt") as f:
        for line in f:
            # print(line)
            coef = list(map(float, line.split()))
            # print(coef)
            coef_num = len(coef)
            if coef_num == 2:
                equations.append(Equation(*coef))
            elif coef_num == 3:
                equations.append(QuadraticEquation(*coef))
            elif coef_num == 5:
                a, w, b, v, c = coef
                equations.append(BiQuadraticEquation(a, b, c))

    # for e in equations:
    #     print(e)
    #     print(e.solve())

    equations_0 = [] # не мають розв’язків;
    equations_1 = [] # мають один розв’язок;
    equations_2 = [] # мають два розв’язки;
    equations_3 = [] # мають три розв’язки;
    equations_4 = [] # мають чотири розв’язки;
    equations_inf = [] # мають нескінченну кількість розв’язків.

    for e in equations:
        sols = e.solve()
        if sols == Equation.INF:
            equations_inf.append(e)
        else:
            sols_num = len(sols)
            if sols_num == 0:
                equations_0.append(e)
            elif sols_num == 1:
                equations_1.append(e)
            elif sols_num == 2:
                equations_2.append(e)
            elif sols_num == 3:
                equations_3.append(e)
            elif sols_num == 4:
                equations_4.append(e)


    print("\n\nне мають розв’язків")
    for e in equations_0:
        print(e)
        print(e.solve())

    print("\n\nмають один розв’язок")
    for e in equations_1:
        print(e)
        print(e.solve())

    print("\n\nмають два розв’язки")
    for e in equations_2:
        print(e)
        print(e.solve())

    print("\n\nмають три розв’язки")
    for e in equations_3:
        print(e)
        print(e.solve())

    print("\n\nмають чотири розв’язки")
    for e in equations_4:
        print(e)
        print(e.solve())

    print("\n\nмають нескінченну кількість розв’язків")
    for e in equations_inf:
        print(e)
        print(e.solve())

