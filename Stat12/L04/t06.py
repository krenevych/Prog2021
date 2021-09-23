n = int(input())

# 21   int((21)**0.5) = int(4.6) = 4
# 3 * 7
# q = int((n)**0.5)
# a1 > q, a2 > q: a1 * a2 > q**2 = n


for i in range(2, int(n**0.5) + 1):
    if n % i == 0:  # число n поділилося на i без остачі
        print(0)
        break
else:
    print(1)