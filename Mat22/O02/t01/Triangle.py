from turtle import *

class Triangle:
    def __init__(self, color, *coords):
        assert len(coords) == 6
        self.coords = list(coords)
        self.color = color

    def draw(self):
        x1, y1 = self.coords[ :2]
        x2, y2 = self.coords[2:4]
        x3, y3 = self.coords[4: ]

        pencolor(self.color)

        up()
        setpos(x1, y1)
        down()
        goto(x2, y2)
        goto(x3, y3)
        goto(x1, y1)
        up()

if __name__ == "__main__":
    reset()
    t = Triangle("dark violet",
                 50, 50, 200, 50, 150, 200)

    t2 = Triangle("spring green",
                 50, 50, 200, 50, 150, 200)
    t.draw()
    mainloop()

