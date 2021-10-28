# 0 * 4 = 0
# 1 * 4 = 0 + 4 = 4
# 2 * 4 = 1 * 4 + 4 = 0 + 4 + 4
# 3 * 4 = 2 * 4 + 4 = ...
# ....
# n * 4 = (n-1) * 4 + 4


# n * m = (n-1) * m + m, n >=1

# mult(n, m) = mult(n-1, m) + m, n >=1
# mult(0, m) = 0, (n==0)

def mult(n, m):
    if n >= 1:
        a = mult(n - 1, m)
        return a + m
    else:
        return 0

print(mult(3, 4))
