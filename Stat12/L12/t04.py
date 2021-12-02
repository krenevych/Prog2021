def sqr_a(x):
    return 0


def sqr_b(x):
    eps = 0.000001
    a = x / 2
    while abs(a**2 - x) >= eps:
        a = 0.5 * (a + x / a)
        # print(x, a**2, abs(a**2 - x))

    return a


if __name__ == "__main__":
    x = 13
    print(f"sqr_a({x}) =", sqr_a(x))
    print(f"sqr_b({x}) =", sqr_b(x))
    print(f"  {x}**0.5 =", x ** 0.5)
