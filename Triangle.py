import random

class Triangle:
    def __init__(self, edge_length, start_x, start_y, depth, colours):

        self.edge_length = edge_length
        self.start_x = start_x
        self.start_y = start_y
        self.depth = depth
        self.colours = colours
    
    def __triangle(self, turtle, length, depth):
        if depth == 0:
            return
        # improve flexibility by not hard coding array size
        colour = self.colours[random.randint(0,len(self.colours)-1)]
        turtle.color(colour)

        for x in range(depth):
            for i in range(3):
                turtle.forward(length)
                turtle.left(120)
                self.__triangle(turtle,length/2,depth-1)
            return
        
    def draw(self, turtle):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(self.start_x,self.start_y)
        turtle.pendown()
        self.__triangle(turtle,self.edge_length,self.depth)
