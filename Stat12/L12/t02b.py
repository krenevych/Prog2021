import math
def custom_cos(x):
    eps = 0.001
    S = 1
    a = 1
    n = 0
    while abs(a) >= eps:
        n += 1
        a *= -(x ** 2) / (2 * n *(2 * n - 1))
        S += a
        # print(S)
    return S

if __name__ == "__main__":
    x = 0.7
    print(f"  math.cos({x}) =", math.cos(x))
    print(f"custom_cos({x}) =", custom_cos(x))
