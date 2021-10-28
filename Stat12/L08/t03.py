# n = 0:                   1
# n = 1:                 1   1
# n = 2:               1   2   1
# n = 3:             1   3   3   1
# n = 4:           1   4   6   4   1
# n = 5:        1   5   10   10  5   1
# n = 6:      1   6   15  20  15   6   1

# (a + b)^n = C(n, 0)a^n + C(n, 1)a^(n-1)b + ... C(n, n)b^n

# C(3, 1) = C(2, 0) + C(2, 1)
# C(4, 2) = C(3, 1) + C(3, 2)

# C(n, 0) = 1, C(n, n) = 1
# C(n, k) = C(n-1, k-1) + C(n-1, k)

def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return C(n-1, k-1) + C(n-1, k)

N = int(input())
for n in range(N+1):
    for k in range(n+1): # рядок
        print(C(n, k), end=" ")
    print()

# print(C(30, 15))