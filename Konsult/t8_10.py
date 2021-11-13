def permut(n, current, permuted: list):
    if len(permuted) == n:
        print(*permuted)
    else:
        for i in range(current):
            new_permuted = permuted[:]
            new_permuted.insert(i, current)
            permut(n, current + 1, new_permuted)


permut(3, 1, [])
