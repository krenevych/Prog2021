
f = open("output13_3.txt", "w")

for i in range(1, 100):
    print(str(i)*i, file=f)

f.close()
