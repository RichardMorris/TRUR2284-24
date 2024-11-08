from turtle import Turtle
from Triangle import Triangle

bob = Turtle()
bob.getscreen().setup(width=600, height=600, startx=0, starty=0)

colours = ["blue","red","magenta","black","yellow"]

start_x = -250
start_y = -250
start_length = 500

tri = Triangle(500, -250, -250, 1, colours[1:2])
tri.draw(bob)

tri2 = Triangle(250, -250, -250, 1, colours[2:3])
tri2.draw(bob)

Triangle(125, -250, -250, 2, colours[3:4]).draw(bob)

bob.getscreen().mainloop()