def S(n):
    s = 1
    yield s
    for i in range(2, n + 1):
        s += 1/i
        yield s


if __name__ == '__main__':

    for r in S(5):
        print(r)


    # print(S(5)) # 2.283333333333333
