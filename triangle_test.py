import unittest
from Triangle import *

class TurtleMock:
    def __init__(self):
        self.called = []
    def forward(self, length):
        self.called.append(("forward", length))
    def left(self, angle):
        self.called.append(("left", angle))
    def color(self, colour):
        self.called.append(("color", colour))
    def speed(self, speed):
        self.called.append(("speed", speed))
    def penup(self):
        self.called.append(("penup"))
    def pendown(self):
        self.called.append(("pendown"))
    def goto(self, x, y):
        self.called.append(("goto", x, y))


class TestTriangle(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(Triangle(500, -250, -250, 1, ["blue"]).edge_length, 500)
        self.assertEqual(Triangle(500, -250, -250, 1, ["blue"]).start_x, -250)
        self.assertEqual(Triangle(500, -250, -250, 1, ["blue"]).start_y, -250)
        self.assertEqual(Triangle(500, -250, -250, 1, ["blue"]).depth, 1)
        self.assertEqual(Triangle(500, -250, -250, 1, ["blue"]).colours, ["blue"])

    def test_triangle_draw_level1(self):
        tri = Triangle(500, -250, -250, 1, ["blue"])
        turtle = TurtleMock()
        tri.draw(turtle)
        self.assertEqual(len(turtle.called),11)
        self.assertEqual(turtle.called[0], ("speed", 0))
        self.assertEqual(turtle.called[1], ("penup"))
        self.assertEqual(turtle.called[2], ("goto", -250, -250))
        self.assertEqual(turtle.called[3], ("pendown"))
        self.assertEqual(turtle.called[4], ("color", "blue"))
        self.assertEqual(turtle.called[5], ("forward", 500))
        self.assertEqual(turtle.called[6], ("left", 120))
        self.assertEqual(turtle.called[7], ("forward", 500))
        self.assertEqual(turtle.called[8], ("left", 120))
        self.assertEqual(turtle.called[9], ("forward", 500))
        self.assertEqual(turtle.called[10], ("left", 120))

    def test_triangle_draw_level2(self):
        tri = Triangle(500, -250, -250, 2, ["blue"])
        turtle = TurtleMock()
        tri.draw(turtle)
        self.assertEqual(len(turtle.called),32)

        self.assertEqual(turtle.called[0], ("speed", 0))
        self.assertEqual(turtle.called[1], ("penup"))
        self.assertEqual(turtle.called[2], ("goto", -250, -250))
        self.assertEqual(turtle.called[3], ("pendown"))

        self.assertEqual(turtle.called[4], ("color", "blue"))
        self.assertEqual(turtle.called[5], ("forward", 500))
        self.assertEqual(turtle.called[6], ("left", 120))

        self.assertEqual(turtle.called[7], ("color", "blue"))
        self.assertEqual(turtle.called[8], ("forward", 250))
        self.assertEqual(turtle.called[9], ("left", 120))
        self.assertEqual(turtle.called[10], ("forward", 250))
        self.assertEqual(turtle.called[11], ("left", 120))
        self.assertEqual(turtle.called[12], ("forward", 250))
        self.assertEqual(turtle.called[13], ("left", 120))
        
        self.assertEqual(turtle.called[14], ("forward", 500))
        self.assertEqual(turtle.called[15], ("left", 120))

        self.assertEqual(turtle.called[16], ("color", "blue"))
        self.assertEqual(turtle.called[17], ("forward", 250))
        self.assertEqual(turtle.called[18], ("left", 120))
        self.assertEqual(turtle.called[19], ("forward", 250))
        self.assertEqual(turtle.called[20], ("left", 120))
        self.assertEqual(turtle.called[21], ("forward", 250))
        self.assertEqual(turtle.called[22], ("left", 120))

        self.assertEqual(turtle.called[23], ("forward", 500))
        self.assertEqual(turtle.called[24], ("left", 120))

        self.assertEqual(turtle.called[25], ("color", "blue"))
        self.assertEqual(turtle.called[26], ("forward", 250))
        self.assertEqual(turtle.called[27], ("left", 120))
        self.assertEqual(turtle.called[28], ("forward", 250))
        self.assertEqual(turtle.called[29], ("left", 120))
        self.assertEqual(turtle.called[30], ("forward", 250))
        self.assertEqual(turtle.called[31], ("left", 120))


if __name__ == '__main__':
    unittest.main()