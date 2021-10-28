# def nsd(a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     elif a >= b:
#         return nsd(a % b, b)
#     else:
#         return nsd(b % a, a)

def nsd(n, m):
    if n < m:
        return nsd(m, n)
    if m == 0:
        return n
    else:
        return nsd(m, n % m)

n, m = [int(el) for el in input().split()]
print(nsd(n, m))
