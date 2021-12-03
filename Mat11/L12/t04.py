def sqr_a(x):
    eps = 0.00000001
    a = x / 2
    while True:
        a_prev = a
        a = 0.5 * (a + x / a)
        # print(x, a, a_prev, abs(a - a_prev))
        if abs(a - a_prev) < eps:
            break

    return a

def sqr_b(x):
    eps = 0.00000001
    a = x / 2
    while abs(a**2 - x) >= eps:
        a = 0.5 * (a + x / a)
        # a**2 ~ x
        # print(x, a, a**2, abs(a**2 - x))

    return a

if __name__ == "__main__":
    x = 2
    print(f"sqr_a({x}) =", sqr_a(x))
    print(f"sqr_b({x}) =", sqr_b(x))
    print(f"({x}**0.5) =", x**0.5)