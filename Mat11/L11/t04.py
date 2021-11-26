N = int(input("Введіть кількість рисок дробу у ланцюговому дробі "))

f = 1
for n in range(1, N+1):
    f = 1 + 1 / f

print(f)