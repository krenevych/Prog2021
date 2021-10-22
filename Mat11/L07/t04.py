
def nsd(n, m):
    if n < m:
        n, m = m, n

    while m != 0:
        p = n % m
        n, m = m, p

    return n

n, m = [int(el) for el in input().split()]
res = nsd(n, m)
print(res)

