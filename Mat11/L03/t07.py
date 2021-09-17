# Записати задане натуральне число n в зворотному порядку

n = int(input())
inv = 0
orig_n = n
while n > 0:
    last = n % 10
    inv = inv * 10 + last
    n = n // 10

if inv == orig_n:
    print("Yes")
else:
    print("No")