n = int(input())
A = [int(a) for a in input().split()]

for i in range(n - 1, 0, -1):
    for j in range(0, i):
        if A[j] > A[j + 1]:
            A[j], A[j+1] = A[j+1], A[j]
    # for el in A:
    #     print(el, end=" ")
    # print()

    print(*A)




