# Обчислити відношення добутку цифр
# натурального числа до їх суми.
# 364
n = int(input())

mult = 1
suma = 0
while n > 0:
    last = n % 10
    suma += last
    mult *= last
    n = n // 10

res = mult / suma

print("%0.3f" % res)
