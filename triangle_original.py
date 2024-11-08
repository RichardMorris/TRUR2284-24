import random

#import ipyturtle3 as turtle
#from ipyturtle3 import hold_canvas
#myCanvas=Turtle.Canvas(width=800,height=800)
#turtle.display(myCanvas)
#myTS=Turtle.TurtleScreen(myCanvas)
#bob=Turtle.turtle()
#myTS=Turtle.getscreen(bob)
#myTS.clear()

# Modified code to work outside Juypter labs
from turtle import Turtle
bob = Turtle()
bob.getscreen().setup(width=600, height=600, startx=0, starty=0)

colours = ["blue","red","magenta","black","yellow"]

bob.speed(0)
bob.penup()
bob.goto(-250,-250)
bob.pendown()
start_length = 500
def triangle(turtle,start,stop,colour):
    if stop == 0:
        return
    colour = colours[random.randint(0,4)]
    turtle.color(colour)
    for x in range(stop):
        for i in range(3):
            turtle.forward(start)
            turtle.left(120)
            triangle(turtle,start/2,stop-1,colour)
        return

triangle(bob,start_length,6,colours)
bob.getscreen().mainloop()
