def gen(x, N):
    yield 1
    a = 1
    for n in range(1, N + 1):
        a *= x / n
        yield a

if __name__ == '__main__':
    for a in gen(1, 50):
        print(a)

    # print(gen(1, 50))

    # 3.2879494166331567e-65