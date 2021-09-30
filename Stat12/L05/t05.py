a = [int(el) for el in input().split()]
b = [int(el) for el in input().split()]

# [5, 1, 2, 6]
# [x0, y0, x1, y1]
# [ 0,  1,  2,  3]

v = [a[2] - a[0], a[3] - a[1]]  # (v[0], v[1])
u = [b[2] - b[0], b[3] - b[1]]  # (u[0], u[1])

len_v = (v[0] ** 2 + v[1] ** 2) ** 0.5
len_u = (u[0] ** 2 + u[1] ** 2) ** 0.5

v_plus_u = [v[0] + u[0], v[1] + u[1]]

dot_product = v[0] * u[0] + v[1] * u[1]
cross_product = u[1] * v[0] - u[0] * v[1]

print("%0.6f %0.6f" % (len_v, len_u))
print("%0.6f %0.6f" % (v_plus_u[0], v_plus_u[1]))
print("%0.6f %0.6f" % (dot_product, cross_product))
print("%0.6f" % (0.5 * abs(cross_product)))
