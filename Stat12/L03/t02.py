# Для заданого натурального числа n
# вивести всі степені двійки менші за n.

# n = 7: 2 4
# 2**3 = 2 * 2 * 2
n = int(input())

res = 2
while res < n:
    print(res, end=" ")
    res *= 2



