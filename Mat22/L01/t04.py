# Розкласти задане трицифрове число на цифри.

a = int(input())   # 456

a = abs(a)

o = a % 10
d = a // 10 % 10
s = a // 100

print(s)
print(d)
print(o)
