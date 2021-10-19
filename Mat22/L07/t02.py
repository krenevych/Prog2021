# n = 10
# a_n: 2 36 52 5 2 77 125 13 625 256

def isFullSqr(k):
    sqrt = k ** 0.5
    sqrt2 = int(sqrt) ** 2
    return sqrt2 == k

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
an = [int(el) for el in input().split()]
fullSqrs = []
pow5s = []
primes = []
for el in an:
    if isFullSqr(el):
        fullSqrs.append(el)
    if isPow5(el):
        pow5s.append(el)
    if isPrime(el):
        primes.append(el)

print("Повні квадрати:", *fullSqrs)
print("Cтепені п’ятірки:", *pow5s)
print("Прості числа:", *primes)
