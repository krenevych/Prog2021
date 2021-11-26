N = int(input("N = "))

#         u
#           v
#             w
# 0 1 1 2 4 7 13 24 44 81
#
# 0 1 2 3 4 5 6  7  8  9

u, v, w = 0, 1, 1

for k in range(3, N+1):
    w, v, u = w + v + u, w, v # 13, 7, 4

print(w)

