#Troy Witmer

import turtle


bob = turtle.Turtle()
bob.pensize(3)
bob.color("black","yellow")
x = 100

bob.begin_fill()
for i in range(3):
    bob.forward(x)
    bob.left(120)
bob.end_fill()

bob.forward(x / 2)
bob.left(60)

bob.fillcolor("black")
bob.begin_fill()
for i in range(3):
    bob.forward(x / 2)
    bob.left(120)
bob.end_fill()

turtle.done()