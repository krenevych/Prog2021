def sqr_a(x):
    assert x >= 0
    eps = 0.000001
    a = x / 2
    while True:
        a_prev = a
        a = 0.5 * (a + x / a)
        if abs(a - a_prev) < eps:
            break

        # print(x, a, a_prev, abs(a - a_prev))

    return a



def sqr_b(x):
    assert x >= 0
    eps = 0.000001
    a = x / 2
    while abs(a**2 - x) >= eps:
        a = 0.5 * (a + x / a)
        # print(x, a**2, abs(a**2 - x))

    return a


if __name__ == "__main__":
    x = 14
    print(f"sqr_a({x}) =", sqr_a(x))
    print(f"sqr_b({x}) =", sqr_b(x))
    print(f"  {x}**0.5 =", x ** 0.5)
