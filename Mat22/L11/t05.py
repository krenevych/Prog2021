n = int(input("n = ? "))

u = 0
v = 1
w = 1

# for k in range(3, n+1):
#     q = u + v + w
#     u = v
#     v = w
#     w = q

for k in range(3, n+1):
    w, v, u = u + v + w, w, v

print(w)
