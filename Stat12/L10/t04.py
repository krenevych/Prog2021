from base import readMatrix

a = readMatrix(2, float)

detA = a[0][0] * a[1][1] - a[0][1] * a[1][0]
detX = a[0][2] * a[1][1] - a[0][1] * a[1][2]
detY = a[0][0] * a[1][2] - a[0][2] * a[1][0]

x = detX / detA
y = detY / detA

print("%0.3f" % x)
print("%0.3f" % y)

# printMatrix(A)