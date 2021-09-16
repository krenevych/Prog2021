# Підрахувати кількість цифр цілого невід'ємного числа n.

#      => 4

n = int(input())
counter = 0
if n == 0:
    counter = 1

while n > 0:
    counter += 1
    n //= 10

print(counter)

