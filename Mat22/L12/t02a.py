from math import sin

def custom_sin(x):
    eps = 0.000001
    a = x
    S = x
    n = 0
    # for n in range(1, N + 1):
    while abs(a) >= eps:
        n += 1
        a *= - x ** 2 / (2 * n * (2 * n + 1))
        S += a

    return S


x = float(input("x = "))
print(f"custom.sin({x})=", custom_sin(x))
print(f"  math.sin({x})=", sin(x))
