# 7! = 1 * 1 * 2 * 3 * 4 * 5 * 6 * 7
# 0! = 1
# fact(n) = fact(n-1) * n, n >= 1
# fact(0) = 1

def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n

print(fact(5))
