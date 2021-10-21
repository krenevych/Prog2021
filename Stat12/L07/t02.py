# 7
# 23 125 16 13 625 11 12

# 16, 625
# 125, 625
# 23, 13, 11

def isFullSquare(k):
    k_2 = int(k ** 0.5) ** 2
    return k == k_2

def isPow5(k):
    p = 1
    while p < k:
        p *= 5

    return k == p

def isPrime(k):
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False

    return True

# n = int(input())
a = [int(el) for el in input().split()]
fullSquares = []
pow5s = []
primes = []
for el in a:
    if isFullSquare(el):
        fullSquares.append(el)

    if isPow5(el):
        pow5s.append(el)

    if isPrime(el):
        primes.append(el)

print("Повні квадрати:", *fullSquares)
print("степені п’ятірки:", *pow5s)
print("прості числа:", *primes)




