# 1. Описати підпрограму перевірки чи є число простим
# 2. Опишемо головну підпрограму, яка буде виводити пари "близнюків" із відрізка [n,2n],
# 3. Використаємо описані підпрограми для розв'язання задачі

def isPrime(k):
    for i in range(2, int(k ** 0.5) + 1):
        if k % i == 0:
            return False

    return True

def showTwins(n):
    for i in range(n, 2 * n - 1):
        if isPrime(i) and isPrime(i + 2):
            print(i, i + 2)

n = int(input("Уведіть n? "))
showTwins(n)

