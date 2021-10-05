n = int(input())

freq = [0] * 10
# freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while n > 0:
    d = n % 10
    freq[d] += 1
    n //= 10

print(*freq)
