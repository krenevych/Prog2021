# Для заданого натурального числа n
# вивести всі степені двійки менші за n.

# n = 127: 2 4 8 16 32 64
n = int(input())

pow2 = 2
while pow2 < n:
    print(pow2, end=" ")
    pow2 *= 2 # pow2 = pow2 * 2