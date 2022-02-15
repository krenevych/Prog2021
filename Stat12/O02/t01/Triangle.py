from turtle import *

class Triangle:
    def __init__(self, *coords):
        assert len(coords) == 6
        self.coords = list(coords)
        self.color = "black"

    def setColor(self, color):
        self.color = color

    def draw(self):
        x1, y1 = self.coords[:2]
        x2, y2 = self.coords[2:4]
        x3, y3 = self.coords[4:]

        pencolor(self.color)
        up()
        setpos(x1, y1)
        down()
        goto(x2, y2)
        goto(x3, y3)
        goto(x1, y1)
        up()


if __name__ == "__main__":
    t = Triangle(100, 100, 300, 100, 200, 300)
    t.setColor("#ed648d")
    t.draw()

    mainloop()
