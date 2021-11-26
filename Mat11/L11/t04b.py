N = int(input("Введіть кількість рисок дробу у ланцюговому дробі "))

f = 2
for n in range(1, N + 1):
    f = 2 + 1 / f

print(f - 1)
