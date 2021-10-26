# 4 * 2 = 2 + 2 + 2 + 2         = 2 + 3 * 2
# 5 * 2 = 2 + 2 + 2 + 2 + 2     = 2 + 4 * 2
# 6 * 2 = 2 + 2 + 2 + 2 + 2 + 2 = 2 + 5 * 2
# m * n = n + (m-1) * n
# mult(m, n) = n + mult(m - 1, n), m, n > 0
# 0 * n = 0
# m * 0 = 0

def mult(m, n):
    if n == 0 or m == 0:
        return 0
    else:
        res_m = mult(m - 1, n)
        res = n + res_m
        return res

print(mult(6, 2))



