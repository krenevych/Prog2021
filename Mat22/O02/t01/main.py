from turtle import mainloop
from Triangle import Triangle
from random import randint

colors = [
    "royal blue",
    "dark goldenrod",
    "lime",
    "blue",
    "orange"
]

triangles = []  # список трикутників

for i in range(100):  # номер трикутника
    coords = []
    for j in range(6):  # кордината
        x = randint(-300, 300)
        coords.append(x)

    color_num = randint(0, len(colors) - 1)
    color = colors[color_num]

    t = Triangle(color, *coords)
    triangles.append(t)

for t in triangles:
    t.draw()

mainloop()
