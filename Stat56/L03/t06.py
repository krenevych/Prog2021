# Записати задане натуральне число n в зворотному порядку.
# 712    ->   217

n = int(input())

inv = 0
while n > 0:
    last = n % 10
    n = n // 10
    inv = inv * 10 + last

print(inv)
