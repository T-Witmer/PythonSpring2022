#Troy Witmer

import turtle

bob = turtle.Turtle()
radius = 50
n = int(input("sides "))
pi = 3.14159
side = 2 * pi * radius / n 

for _ in range(n):
    bob.forward(side)
    bob.left(360 / n)

turtle.done()
