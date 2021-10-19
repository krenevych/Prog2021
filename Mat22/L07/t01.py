def isPrime(k):
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False
    return True


n = int(input())
for i in range(n, 2 * n - 1):
    if isPrime(i) and isPrime(i+2):
        print(f"{i}, {i+2}")
