from Triangle import Triangle
from turtle import mainloop, speed
from random import randint

if __name__ == '__main__':
    speed(0)

    colors = [
        "light gray",
        "aquamarine",
        "olive",
        "crimson",
        "purple",
        "yellow green"
    ]

    COORD_X_RANGE = (-300, 300)
    COORD_Y_RANGE = (-400, 400)

    triangles = []
    for i in range(100):
        x1 = randint(*COORD_X_RANGE)
        x2 = randint(*COORD_X_RANGE)
        x3 = randint(*COORD_X_RANGE)
        y1 = randint(*COORD_Y_RANGE)
        y2 = randint(*COORD_Y_RANGE)
        y3 = randint(*COORD_Y_RANGE)
        t = Triangle(x1, y1, x2, y2, x3, y3)
        pensize = randint(1, 10)
        t.setPenSize(pensize)

        col_num = randint(0, len(colors) - 1)
        color = colors[col_num]
        t.setColor(color)

        triangles.append(t)

    for triangle in triangles:
        triangle.draw()

    mainloop() # щоб не закривалось вікно
