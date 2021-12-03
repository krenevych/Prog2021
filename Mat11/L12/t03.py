
a = int(input("a = "))
u, v, w = 1, 1, 1
n = 2
# for n in range(3, N+1):
while True:
    n += 1
    w, v, u = v + u, w, v
    # print(n, w)
    if w >= a:
        break

# print("Відповідь: ", n-1, v, w)
print("Відповідь: ", n-1)

