def sqr_b(x):
    assert x >= 0
    eps = 0.000001
    a = x / 2
    while True:
        a = 0.5 * (a + x / a)
        # print(a, a**2)
        if abs(a ** 2 - x) < eps:
            break

    return a

def sqr_a(x):
    assert x >= 0
    eps = 0.000001
    a = x / 2

    while True:
        a_prev = a
        a = 0.5 * (a + x / a)
        # print(a, a_prev, a - a_prev)
        if abs(a - a_prev) < eps:
            break

    return a

if __name__ == "__main__":
    x = float(input("x = "))
    print(f"sqr_a({x})  =", sqr_a(x))
    print(f"sqr_b({x})  =", sqr_b(x))
    print(f"{x}**0.5    =", x**0.5)