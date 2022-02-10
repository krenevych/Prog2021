from QuadraticEquation import QuadraticEquation

equations = []
with open("input03.txt") as f:
    for line in f:
        try:
            a, b, c = map(float, line.split())
            # print(a, b, c)
            e = QuadraticEquation(a, b, c)
            equations.append(e)
        except ValueError:
            break

equations_0 = []    # список рівнянь, що не мають розв’язків;
equations_1 = []    # список рівнянь, що мають один розв’язок;
equations_2 = []    # список рівнянь, що мають два розв’язки;
equations_inf = []  # список рівнянь, що мають нескінченну кількість розв’язків.


for e in equations:
    sol_num = e.solutions_number()
    if sol_num == 0:
        equations_0.append(e)
    elif sol_num == 1:
        equations_1.append(e)
    elif sol_num == 2:
        equations_2.append(e)
    else:
        equations_inf.append(e)

print("\nсписок рівнянь, що не мають розв’язків")
print("======================================")
for e in equations_0:
    e.show()
    print(e.solutions())

print("\nсписок рівнянь, що мають один розв’язок")
print("======================================")
for e in equations_1:
    e.show()
    print(e.solutions())

print("\nсписок рівнянь, що мають два розв’язки")
print("======================================")
for e in equations_2:
    e.show()
    print(e.solutions())

print("\nсписок рівнянь, що мають нескінченну кількість розв’язків")
print("======================================")
for e in equations_inf:
    e.show()
    print(e.solutions())

print("\n=====================================\n")
print("рівняння, що має	найменший розв’язок;")
eq_with_min_sol = equations_1[0]
min_sol = eq_with_min_sol.solutions()[0]
for e in equations_1:
    x = e.solutions()[0]
    if min_sol > x:
        min_sol = x
        eq_with_min_sol = e

eq_with_min_sol.show()
print(min_sol)