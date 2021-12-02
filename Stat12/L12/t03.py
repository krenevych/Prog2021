u, v, w = 1, 1, 1

N = 10
n = 2
a = int(input())
# for i in range(3, N+1):
while True:
    n += 1
    w, v, u = u + v, w, v
    # print(n, w)
    if w > a:
        break

print("Відповідь: ", n-1, v, w)