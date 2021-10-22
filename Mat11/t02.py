# n = 8
# 35 13 125 36 11 13 9 625
# повні квадрати: 36 9 625
# степені 5: 125 625
# прості числа 13 11 13

def isFullSquare(k):
    pass

def isPower5(k):
    pass

def isPrime(k):
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True

a = [int(el) for el in input().split()]
fullSquares = []
power5s = []
primes = []

for el in a:
    if isFullSquare(el):
        fullSquares.append(el)

    if isPower5(el):
        power5s.append(el)

    if isPrime(el):
        primes.append(el)

print("Повні квадрати:", *fullSquares)
print("степені 5:", *power5s)
print("прості числа:", *primes)

