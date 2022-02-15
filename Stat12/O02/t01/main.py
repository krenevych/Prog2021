from Triangle import Triangle
from random import randint

colors = [
    "red",
    "green",
    "blue",
    "#F4A460",
    "dark slate gray",
    "#800080",
    "#9370DB"
]

triangles = []
for i in range(100):
    coords = []
    for i in range(6):
        x = randint(-300, 300)
        coords.append(x)

    # print(coords)
    t = Triangle(*coords)

    num_color = randint(0, len(colors)-1)
    t.setColor(colors[num_color])
    triangles.append(t)

for t in triangles:
    t.draw()
