# n = 0:                  1
# n = 1:               1     1
# n = 2:             1    2    1
# n = 3:           1   3     3    1
# n = 4:         1   4    6     4   1
# n = 5:      1   5    10    10   5    1
# n = 6:    1                             1

# (a + b) ^ 4 = a^4 + 4 a^3 b^1 + 6 a^2 b^2 + 4 a^1 b^3 + b^4
# (a + b) ^ 4 = C(4, 0) a^4 + C(4, 1) a^3 b^1 + C(4, 2) a^2 b^2 + C(4, 3) a^1 b^3 + C(4, 4)b^4
# C(n, 0) = 1, C(n,n) = 1 - тривіальний випадок
# C(n, k) = C(n-1, k-1) + C(n-1, k) - рекурернтний виклик

# C(4, 2) = C(3, 1) + C(3, 2)
# C(5, 4) = C(4, 3) + C(4, 4)

def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return C(n - 1, k - 1) + C(n - 1, k)

# c = C(5, 2)
# print(c)

N = int(input())
for n in range(N+1):
    for k in range(n+1):
        print(C(n, k), end=" ")
    print()