N = int(input("Введіть порядок визначника "))

u = 2  # D_n-2
v = 1  # D_n-1
for n in range(3, N + 1):
   v, u = 2 * v - 3 * u, v

print(f"D({N}) = {v}")