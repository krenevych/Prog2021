# p = 13 31
# 13  31

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def inverse(n):
    inv = 0
    while n > 0:
        inv = inv * 10 + n % 10
        n //= 10
    return inv

k = int(input())

hapy_prime_num = 0
i = 2
while True:
    inv = inverse(i)
    if i != inv and isPrime(i) and isPrime(inv):
        hapy_prime_num += 1
        if hapy_prime_num == k:
            print(i)
            break

    i += 1

