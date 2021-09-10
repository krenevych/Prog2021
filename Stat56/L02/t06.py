x, y = map(float, input().split())

if x > 0 and y > 0:
    print(1)
else:
    if x < 0 and y > 0:
        print(2)
    else:
        if x < 0 and y < 0:
            print(3)
        else:
            if x > 0 and y < 0:
                print(4)
            else:
                print(0)
