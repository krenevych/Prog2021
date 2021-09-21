# Обчислити відношення добутку цифр
# натурального числа до їх суми
# 234
n = int(input())
suma = 0
mult = 1
while n > 0:
    last = n % 10
    suma += last
    mult *= last
    n //= 10

print("%0.3f" % (mult / suma))
