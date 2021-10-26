# def nsd(n, m):
#     if n < m:
#         n, m = m, n
#
#     while m > 0:
#         p = m
#         m = n % m
#         n = p
#
#     return n

def nsd(n, m):
    if n < m:
        return nsd(m, n)

    if m == 0:
        return n
    else:
        return nsd(m, n % m)


# def nsd(a, b):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     elif a >= b:
#         return nsd(a % b, b)
#     else:
#         return nsd(b % a, a)

n, m = [int(el) for el in input().split()]
print(nsd(n, m))