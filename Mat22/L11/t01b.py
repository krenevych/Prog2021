import math

N = int(input("N = "))
x = float(input("x = "))

x_N = (-1) ** N * x ** (2 * N) / math.factorial(2 * N)
print(x_N)

a = 1
for k in range(1, N + 1):
    a *= - x * x / ((2 * k - 1) * 2 * k)

print(a)
