N = int(input("Введіть порядок визначника: "))

if N == 1:
    print(2)
elif N == 2:
    print(1)
else:
    u, v = 2, 1
    for n in range(3, N + 1):
        v, u = 2 * v - 3 * u, v
    print(v)
