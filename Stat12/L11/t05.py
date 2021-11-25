N = int(input("N = "))

u = 0
v = 1
w = 1
for k in range(3, N + 1):
    w, v, u = u + v + w, w, v

print(w)
