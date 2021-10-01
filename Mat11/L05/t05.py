a = [int(el) for el in input().split()]
b = [int(el) for el in input().split()]
# [a[0], a[1], a[2], a[3]]
# [  x0,   y0,   x1,   y1]

# u = [x1-x0, y1-y0]
u = [a[2] - a[0], a[3] - a[1]]
v = [b[2] - b[0], b[3] - b[1]]

# u = [u[0], u[1]]

len_u = (u[0]**2 + u[1]**2)**0.5
len_v = (v[0]**2 + v[1]**2)**0.5
print("%0.6f %0.6f" % (len_u, len_v))

u_plus_v = [u[0] + v[0], u[1] + v[1]]
print("%0.6f %0.6f" % (u_plus_v[0], u_plus_v[1]))

u_dot_v = u[0]*v[0] + u[1]*v[1]
u_cross_v = u[0]*v[1] - u[1]*v[0]
print("%0.6f %0.6f" % (u_dot_v, u_cross_v))
print("%0.6f" % (abs(u_cross_v) / 2))

