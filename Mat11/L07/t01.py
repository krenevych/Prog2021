# 21
# 21 % 2, 3, 4, 5, 6, 7, 8, ...., 20
# 21 % 2, ...., 21**0.5
# [21**0.5, 21)


def isPrime(k):
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

def findTwins(n):
    for i in range(n, 2 * n - 1):
        if isPrime(i) and isPrime(i + 2):
            print(i, i + 2)

#  40, 42,    41, 43,    42, 44, ....
n = int(input())
findTwins(n)

