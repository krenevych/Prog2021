
n = int(input())

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print(0)
        break
else:
    print(1)
