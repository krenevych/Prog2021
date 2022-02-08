from QuadraticEquation import QuadraticEquation
equations = []

# f = open("input01.txt")
with open("input01.txt") as f:
    for line in f:
        try:
            a, b, c = [float(el) for el in line.split()]
            equations.append(QuadraticEquation(a, b, c))
        except ValueError:
            break

equations_no_solutions  = []  # не мають розв’язків;
equations_one_solutions = []   # мають один розв’язок;
equations_two_solutions = []   # мають два розв’язки;
equations_inf_solutions = []   # мають нескінченну кількість розв’язків.

for eq in equations:
    sol_num = eq.solutions_number()
    if sol_num == 0:
        equations_no_solutions.append(eq)
    elif sol_num == 1:
        equations_one_solutions.append(eq)
    elif sol_num == 2:
        equations_two_solutions.append(eq)
    else:
        equations_inf_solutions.append(eq)

print("Рівняння, що не мають розв'язків:")
for e in equations_no_solutions:
    e.show()
print("Рівняння, що мають один розв'язок:")
for e in equations_one_solutions:
    e.show()
print("Рівняння, що мають два розв'язки:")
for e in equations_two_solutions:
    e.show()
print("Рівняння, що мають нескінченну кількість розв'язків:")
for e in equations_inf_solutions:
    e.show()

eq_with_min_solution = equations_one_solutions[0]
min_solution = eq_with_min_solution.solve()[0]
for eq in equations_one_solutions:
    x = eq.solve()[0]
    # print(x)
    if min_solution > x:
        eq_with_min_solution = eq
        min_solution = x

print("++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++")
eq_with_min_solution.show()
print(min_solution)
