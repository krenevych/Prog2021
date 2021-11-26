N = int(input("N = "))

u, v, w = 0, 1, 1

for k in range(3, N+1):
    w, v, u = w + v + u, w, v # 13, 7, 4

print(w)

