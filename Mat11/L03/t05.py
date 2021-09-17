# Обчислити відношення добутку цифр
# натурального числа до їх суми.
# 364

n = int(input())
dobu = 1
suma = 0
while n > 0:
    last = n % 10
    dobu *= last
    suma += last
    n = n // 10

print("%0.3f" % (dobu/suma))



