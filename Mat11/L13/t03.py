def myprint(*args, **kwargs):
    print(*args)
    print(*args, **kwargs)


f = open("output.txt", "w")
for i in range(1, 10):
    # myprint(str(i) * i, file=f)
    print(str(i) * i, file=f)


f.close()