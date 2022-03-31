import turtle
from Teenagefunctions import *

bob = turtle.Turtle()

drawNgon(bob,6,100)
bob.clear()
bob.reset()
bob.speed(0)
drawSquare(bob,50)
bob.clear()
bob.reset()
bob.speed(0)
drawRow(bob,5,50)
bob.clear()
bob.reset()
bob.speed(0)
drawGrid(bob,5,50)
bob.clear()
bob.reset()
bob.speed(0)
drawStairsright(bob,5,50)
bob.clear()
bob.reset()
bob.speed(0)

turtle.exitonclick()