def S():
    s = 1
    i = 1
    yield s

    while True:
        i += 1
        s += 1/i
        yield s


if __name__ == '__main__':

    for r in S():
        if r > 12:
            break
        print(r)


    # print(S(5)) # 2.283333333333333
