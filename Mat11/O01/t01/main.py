
from QuadraticEquation import QuadraticEquation

equations = []
with open("input02.txt") as f:
    for line in f:
        # print(line, end="")
        try:
            a, b, c = map(float, line.split())
            eq = QuadraticEquation(a, b, c)
            equations.append(eq)
        except ValueError:
            continue









equations0 =   [] # рівняння, що не мають розв’язків;
equations1 =   [] # рівняння, що мають один розв’язок;
equations2 =   [] # рівняння, що мають два розв’язки;
equationsInf = [] # рівняння, що мають нескінченну кількість розв’язків.


for eq in equations:
    solution_number = eq.solution_number()
    if solution_number == 0:
        equations0.append(eq)
    elif solution_number == 1:
        equations1.append(eq)
    elif solution_number == 2:
        equations2.append(eq)
    else:
        equationsInf.append(eq)

print("\n\nрівняння, що не мають розв’язків")
for eq in equations0:
    eq.show()
    print(eq.solutions())

print("\n\nрівняння, що мають один розв’язок")
for eq in equations1:
    eq.show()
    print(eq.solutions())


print("\n\nрівняння, що мають два розв’язки")
for eq in equations2:
    eq.show()
    print(eq.solutions())


print("\n\nрівняння, що мають нескінченну кількість розв’язків")
for eq in equationsInf:
    eq.show()
    print(eq.solutions())