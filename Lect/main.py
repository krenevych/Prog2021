import math
eps = 0.000000001
x = float(input("x = "))

S = 1
a = 1
n = 0

while abs(a) > eps:
    n = n + 1
    a = x / n * a
    S = S + a

print(f"exp({x}) = {S}")
print(f"exp({x}) = {math.exp(x)}")
