# Дано тризначне число. Перевірити чи
# a)	містить воно цифру 2;
# b)	складається лише з парних чисел;
# c)	сума його цифр дорівнює 18.
n = int(input())   # n = 234

o = n % 10
d = n // 10 % 10
s = n // 100

check_a = o == 2 or d == 2 or s == 2
# check_a1 = o == 2 and d == 2 and s == 2
check_a1 = n == 222
check_b = o % 2 == 0 and d % 2 == 0 and s % 2 == 0
check_c = o + d + s == 18

print(s, d, o)
print("contains 2 is: ", check_a)
print("all digits are even: ", check_b)
print("sum of digits is 18 is: ", check_c)