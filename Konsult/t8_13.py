def calculateFib(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs

def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        F1 = 1
        F2 = 0
        for i in range(2, n + 1):
            F1, F2 = F1 + F2, F1

        return F1


def nsd(n, m):
    if n < m:
        return nsd(m, n)

    if m == 0:
        return n
    else:
        return nsd(m, n % m)

while True:
    try:
       n, m = [int(el) for el in input().split()]
    except:
        break

    # fibs = calculateFib(max(n, m))
    # f_n = fibs[n]
    # f_m = fibs[m]
    f_n = Fib(n)
    f_m = Fib(m)
    res = nsd(f_m, f_n)
    print(res)

