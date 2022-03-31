# Troy Witmer

import turtle

bob = turtle.Turtle()
ann = turtle.Turtle()

bob.pensize(3)
bob.shape("circle")
bob.left(90)
bob.forward(100)
bob.setpos(-50,100)
bob.right(90)
bob.forward(100)

ann.pensize(3)
ann.shape("circle")
ann.penup()
ann.setpos(50,100)
ann.right(90)
ann.pendown()
ann.left(15)
ann.forward(103)
ann.left(150)
ann.forward(103)
ann.right(150)
ann.forward(103)
ann.left(150)
ann.forward(103)

turtle.done()