#Chapter 5
#Python Turtles

#5.1 Hello Little Turtles

#   turtle.Screen() creates a graphic window
#   turtle.Turtle() creates a turtle, Assign it to a variable for the turtles name
#   EX: alex = turtle.Turtle() creates a turtle named alex
#   .forward moves turtle forwards
#   .left moves turtle left
#   .right moves turtle right

#5.2 Our First turtle program


import turtle
'''
bob = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("red")

bob.forward(100)
bob.left(90)
bob.forward(90)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

wn.exitonclick () # keeps window up until clicked
'''

#5.3 A herd of turtles
'''
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")


tess = turtle.Turtle()           # create tess and set his pen width
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("hotpink")            # set his color

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin so we can see alex

alex.forward(50)                 # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
'''

#5.4 Object Oriented Concepts

# Attributes 

'''
alex.price = 100
tess.price = 400
print( alex.price + tess.price )
'''

# Method

'''
alex.forward(50)
.forward takes a parameter (50)
'''

#5.5 Repetition with a For Loop

# For i in range(10)
# i <- a variable 
# range() <- calls range function (10) will count [0,10)

'''
import turtle
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 50
for _ in range(10):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10
'''
'''
wn = turtle.Screen()

bob = turtle.Turtle()
bob.speed(0)

def drawSquare(T,size):
    for i in range(4):
        T.forward(size)
        T.left(90)
        
for i in range(12):
    bob.color(0+i*.07 , 0 , 1-i*.07)
    drawSquare(bob,100)
    bob.forward(50)
    bob.left(60)
    for i in range(18):
        bob.color(0+i*.03 , 0 , 1-i*.03)
        drawSquare(bob,30)
        bob.forward(30)
        bob.left(20)



turtle.done()
'''
'''
import turtle

wn = turtle.Screen()
bob = turtle.Turtle()
radius = int(input('size of object '))
n = int(input("sides "))
n2 = int(input('side 2 '))
pi = 3.14159
side = 2 * pi * radius / n 
bob.speed(0)

for _ in range(n):
    bob.color(0+_*.007 , 0 , 1-_*.007)
    bob.forward(side)
    bob.left(360 / n)
    for i in range(n2):
        bob.forward(side)
        bob.left(360 / n2)

wn.exitonclick()
'''
#5.6 More turtle methods and observations

'''
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
                     # this is new
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()
'''
