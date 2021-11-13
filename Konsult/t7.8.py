def nsd(N, M):
    if N < M:
        N, M = M, N
    while M > 0:
        N, M = M, N % M
    return N


def nsk(N, M):
    NSD = nsd(N, M)
    return N * M // NSD

A, B = [int(i) for i in input().split()]
# for P in range(A):
#     for Q in range(B):
#         nsd_PQ = nsd(P, Q)
#         nsk_PQ = nsk(P, Q)

counter = 0
for P in range(2, B+1):
    for Q in range(2, B+1):
        NSD_PQ = nsd(P, Q)
        if A == NSD_PQ and B == P * Q // NSD_PQ:
            print(P, Q)
            counter += 1

print(counter)