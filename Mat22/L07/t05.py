def nsd(n, m):
    if n < m:
        n, m = m, n

    while m > 0:
        p = m
        m = n % m
        n = p

    return n


n, m = [int(el) for el in input().split()]
print(nsd(n, m))