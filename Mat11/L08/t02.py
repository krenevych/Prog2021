# m * n = n + n + ... + n
#        ------- m ------
# mult(0, 4) =  0 * 4 = 0
# mult(1, 4) =  1 * 4 = 0 * 4 + 4 = mult(0, 4) + 4 = 4
# mult(2, 4) =  2 * 4 = 1 * 4 + 4 = mult(1, 4) + 4 = 8
# mult(3, 4) =  3 * 4 = 2 * 4 + 4 = mult(2, 4) + 4 = 12

# mult(0, n) = 0
# mult(m, n) = mult(m-1, n) + n, m >= 1

def mult(m, n):
    if m >= 1:
        p = mult(m - 1, n)
        return p + n
    else:
        return 0


res = mult(3, 4)
print(res)