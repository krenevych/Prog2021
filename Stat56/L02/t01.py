"""Записати умови, що істинні тоді й тільки тоді, коли:
a)	натуральне число n – парне;
b)	остання цифра числа n – 0;
c)	сума першої і другої цифри двозначного
натурального числа n – двозначне число."""

n = int(input())  # 34
check_a = n % 2 == 0
print("натуральне число n – парне: ", check_a)

check_b = n % 10 == 0
print("остання цифра числа n – 0: ", check_b)

d = n // 10
o = n % 10
check_c = d + o >= 10

print("сума першої і другої цифри двозначного"
      " натурального числа n – двозначне число:", check_c)
