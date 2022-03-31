# Troy Witmer

import turtle

bob = turtle.Turtle()

bob.shape("turtle")
radius = 100
             
for i in range(12):
    bob.penup()
    bob.forward(radius)
    bob.pendown()
    bob.forward(radius / 10)
    bob.penup()
    bob.forward(radius / 10)
    bob.stamp()
    bob.right(360 / 12)
    bob.setpos(0,0)

bob.hideturtle()

turtle.done()