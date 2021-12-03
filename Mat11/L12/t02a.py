import math

def sin(x):
    eps = 0.0000000000001
    S = x
    a = x
    n = 0
    # for n in range(1, N + 1):
    while abs(a) >= eps:
        n += 1
        a *= - x ** 2 / (2 * n * (2 * n + 1))
        S += a
        print(S)

    return S

if __name__ == "__main__":
    x = math.pi / 6
    print(f"     sin({x}) =", sin(x))
    print(f"math.sin({x}) =", math.sin(x))
