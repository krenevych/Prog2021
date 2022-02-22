from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

equations = []
with open("input01.txt") as f:
    for line in f:
        # print(line)
        coef = list(map(float, line.split()))
        # print(coef)
        if len(coef) == 2:
            b, c = coef
            eq = Equation(b, c)
            equations.append(eq)
        elif len(coef) == 3:
            a, b, c = coef
            eq2 = QuadraticEquation(a, b, c)
            equations.append(eq2)
        elif len(coef) == 5:
            a, w, b, r, c = coef
            eq4 = BiQuadraticEquation(a, b, c)
            equations.append(eq4)


# for e in equations:
#     print(e)
#     print(e.solve())

equation_0 = [] # не мають розв’язків;
equation_1 = [] # •	мають один розв’язок;
equation_2 = [] # •	мають два розв’язки;
equation_3 = [] # •	мають три розв’язки;
equation_4 = [] # •	мають чотири розв’язки;
equation_inf = [] # •	мають нескінченну кількість розв’язків.

for e in equations:

    sols = e.solve()
    if sols == Equation.INF:
        equation_inf.append(e)
    else:
        sol_num = len(sols)
        if sol_num == 0:
            equation_0.append(e)
        elif sol_num == 1:
            equation_1.append(e)
        elif sol_num == 2:
            equation_2.append(e)
        elif sol_num == 3:
            equation_3.append(e)
        elif sol_num == 4:
            equation_4.append(e)

print("========= INF ==================")
for e in equation_inf:
    print(e)
print("========= 0 ==================")
for e in equation_0:
    print(e)
print("========= 1 ==================")
for e in equation_1:
    print(e)
    print(e.solve())
print("========= 2 ==================")
for e in equation_2:
    print(e)
    print(e.solve())

print("========= 3 ==================")
for e in equation_3:
    print(e)
    print(e.solve())
print("========= 4 ==================")
for e in equation_4:
    print(e)
    print(e.solve())