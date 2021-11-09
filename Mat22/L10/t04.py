a = []
for i in range(2):
    row = [float(el) for el in input().split()]
    a.append(row)

# a[0][0] a[0][1] | a[0][2]
# a[1][0] a[1][1] | a[1][2]
#
# det =
# 	  | a[0][0] a[0][1] |
#     | a[1][0] a[1][1] |
#
# detX =
# 	| a[0][2] a[0][1] |
# 	| a[1][2] a[1][1] |
#
# detY =
# 	| a[0][0] a[0][2] |
# 	| a[1][0] a[1][2] |

det =  a[0][0] * a[1][1] - a[0][1] * a[1][0]
detX = a[0][2] * a[1][1] - a[0][1] * a[1][2]
detY = a[0][0] * a[1][2] - a[0][2] * a[1][0]

x = detX / det
y = detY / det

print("%0.3f\n %0.3f" % (x, y))
