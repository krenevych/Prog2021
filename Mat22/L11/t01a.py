N = int(input("N = "))
x = float(input("x = "))

x_k = x ** N / N
print(x_k)

a = x
for k in range(2, N + 1):
    a *= x * (k - 1) / k

print(a)
