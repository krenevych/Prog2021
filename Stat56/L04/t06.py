n = int(input())

prime = True

i = 2
# 21: 3 7
while i < n**0.5 + 1:
    if n % i == 0:
        prime = False
        break
    i += 1

print(1 if prime else 0)