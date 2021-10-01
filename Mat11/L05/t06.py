n = int(input())

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#  0  1  2  3  4  5  6  7  8  9
freq = [0] * 10

while n > 0:
    d = n % 10
    freq[d] += 1
    n //= 10

print(*freq)