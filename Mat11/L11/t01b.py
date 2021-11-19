x = float(input("x = "))
n = int(input("n = "))

a = 1
for k in range(1, n + 1):
    a *= -x * x / ((2 * k - 1) * 2 * k)

print(a)

import math
print((-1)**n * x ** (2*n) / math.factorial(2*n))
