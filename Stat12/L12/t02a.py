import math
def custom_sin(x):
    eps = 0.000001
    S = x
    a = x
    n = 0
    while abs(a) >=eps:
    # for n in range(1, N+1):
        n += 1
        a *= - x ** 2 / (2 * n * (2*n +1))
        S += a
        # print(S)

    return S

if __name__ == "__main__":
    x = 0.7
    print(f"  math.sin({x}) =", math.sin(x))
    print(f"custom_sin({x}) =", custom_sin(x))
