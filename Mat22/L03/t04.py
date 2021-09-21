# Підрахувати кількість цифр цілого невід'ємного числа n.
# n =      2      5     6
n = int(input())
counter = 0

if n == 0:
    counter = 1
else:
    while n > 0:
        counter += 1
        n //= 10

print(counter)
