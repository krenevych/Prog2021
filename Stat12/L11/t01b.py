x = float(input("x = "))  # x = 0.3
n = int(input("n = "))  # n = 20

a = 1
for k in range(1, n + 1):
    a *= -x * x / ((2 * k - 1) * 2 * k)

print(a)

from math import factorial
a_n = (-1) ** n * x ** (2 * n) / factorial(2 * n)
print(a_n)
