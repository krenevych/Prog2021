# Дано тризначне число. Перевірити чи
# a)	містить воно цифру 2;
# b)	складається лише з парних чисел;
# c)	сума його цифр дорівнює 18.
n = int(input())  # n = 32 4
o = n % 10
d = n // 10 % 10
s = n // 100

check_a = o == 2 or d == 2 or s == 2
print(check_a)

check_b = o % 2 == 0 and d % 2 == 0 and s % 2 == 0
print(check_b)

check_c = o + d + s == 18
print(check_c)



