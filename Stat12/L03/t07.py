# Записати задане натуральне число n в зворотному порядку

n = int(input())
inv = 0
n_orig = n
while n > 0:
    last = n % 10
    inv = inv * 10 + last
    n //= 10

if n_orig == inv:
    print("Yes")
else:
    print("No")

