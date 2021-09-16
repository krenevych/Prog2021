# Обчислити відношення добутку цифр натурального числа до їх суми.
# 123412312341234134123412

n = int(input())
dobutok = 1
suma = 0
while n > 0:
    last = n % 10
    dobutok *= last
    suma += last
    n //= 10

res = dobutok / suma

print("%0.3f" % res)

