def P(n):
    a3 = a2 = 1
    a1 = 3

    p0 = 1
    yield p0

    p1 = p0 * 1 / 3
    yield p1

    p = p2 = p1 * 1 / 3
    yield p2

    pow3 = 9
    pow2 = 2
    for k in range(3, n + 1):
        pow3 *= 3
        pow2 *= 2
        a3, a2, a1 = a2, a1, a3 + a2 / pow2
        p = p * a1 / pow3
        yield p

if __name__ == '__main__':
    for p in P(10):
        print(p)



