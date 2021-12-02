u, v, w = 1, 1, 1

N = 10
n = 2
a = int(input())
# for i in range(3, N+1):
while w <= a:
    n += 1
    w, v, u = u + v, w, v
    # print(n, w)


print("Відповідь: ", n-1, v, w)