n = int(input())
inv = 0

while n > 0:
    last = n % 10
    inv = inv * 10 + last
    n //= 10

print(inv)