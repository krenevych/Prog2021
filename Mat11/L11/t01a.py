
x = float(input("x = "))
n = int(input("n = "))

print(x**n / n)

a = x
for k in range(2, n+1):
    a *= x * (k-1) / k

print(a)