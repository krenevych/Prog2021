n = int(input())
# n = 21: 1, 3, 7, 21 => 3
# n = 19: 1, 19 => 19

# q = n**0.5 => q*q = n
# p1, p2 > q
# p1 * p2 > q*q = n

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print(i)
        break
else:
     print(n)

pass

