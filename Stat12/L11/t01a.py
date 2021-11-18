
x = float(input("x = "))  # x = 0.3
n = int(input("n = "))  # n = 20

a = x
for k in range(2, n+1):
    # a = x * (k-1) / k * a
    a *= x * (k-1) / k

print(a)
print(x**n / n)
