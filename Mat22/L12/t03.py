u, v, w = 1, 1, 1
# for k in range(3, 30):
k = 2
a = int(input("a = "))
while True:
    k += 1
    w, v, u = u + v, w, v
    if w > a:
        break
    # print(f"{k}, {w}")

print(k - 1, v, w)
