# Підрахувати кількість цифр цілого невід'ємного числа n.
# n = 1234 5

n = int(input())

if n == 0:
    print(1)
else:
    counter = 0
    while n > 0:
        counter += 1
        n = n // 10

    print(counter)
