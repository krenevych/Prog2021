n = int(input())

if n % 2 == 0:
    print(2)
else:
    check = True

    # 15: 3 5
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            print(i)
            check = False
            break

    if check:
        print(n)

