from math import cos

def custom_cos(x):
    eps = 0.000001
    n = 0
    s = 1
    a = 1
    while abs(a) > eps:
        n += 1
        a *= -(x ** 2) / (2 * n * (2 * n - 1))
        s += a
    return s


if __name__ == "__main__":
    x = float(input("x = "))
    print(f"custom.cos({x})=", custom_cos(x))
    print(f"  math.cos({x})=", cos(x))
