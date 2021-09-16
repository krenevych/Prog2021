# Записати задане натуральне число n в зворотному порядку.
# 712    ->   217

n = int(input())
n_orig = n
inv = 0
while n > 0:
    last = n % 10
    n = n // 10
    inv = inv * 10 + last

if inv == n_orig:
    print("YES")
else:
    print("NO")
