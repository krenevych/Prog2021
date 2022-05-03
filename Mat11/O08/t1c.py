def D(N):
    yield 5
    yield 19

    d2, d1 = 5, 19
    for n in range(3, N + 1):
        d2, d1 = d1, 5 * d1 - 6 * d2
        yield d1

def D_inf():
    yield 5
    yield 19

    d2, d1 = 5, 19
    while True:
        d2, d1 = d1, 5 * d1 - 6 * d2
        yield d1

if __name__ == '__main__':
    # d = D_inf()

    for d in D_inf():
        if d > 1000000:
            break
        print(d)


