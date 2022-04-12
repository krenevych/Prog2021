# 1 1 2 3 5

def Fib():
    yield 1
    yield 1

    F_prev, F_prev_prev = 1, 1
    while True:
        F_prev, F_prev_prev = F_prev + F_prev_prev, F_prev
        yield F_prev


if __name__ == '__main__':
    fib = Fib()
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))
    print(next(fib))

    # for f in Fib():
    #     print(f)
        # if f > 10000:
        #     break
