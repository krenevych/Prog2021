n = int(input())
inv = 0
n_orinal = n
while n > 0:
    last = n % 10
    inv = inv * 10 + last
    n //= 10


if inv == n_orinal:
    print("Yes")
else:
    print("No")