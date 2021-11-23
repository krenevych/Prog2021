N = int(input("N (кількість рисок дробу)= ?"))

f = 1
for k in range(1, N+1):
    f = 1 + 1 / f

print(f)