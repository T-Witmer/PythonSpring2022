#Troy Witmer

import turtle

bob = turtle.Turtle()

#Setup code
radius = 100
dia = radius * 2
extra = radius / 5
bob.pensize(radius / 12)
bob.penup()
bob.backward(radius * 2)
bob.pendown()
color = ["blue" , "black" , "red"] #Top ring colors list
for i in color:  # 3 things in list so draws 3 rings, changing color through list (0 assigned "blue", etc.)
    bob.color(i)
    bob.pendown()
    bob.circle(radius)
    bob.penup()
    bob.forward(dia + extra)

#Reposition
bob.backward(dia * 3 + 3 * (extra))
bob.left(90)
bob.forward(radius)
bob.right(90)
bob.forward(radius + extra / 2)
color = ["yellow" , "green"] 

for i in color:
    bob.color(i)
    bob.pendown()
    bob.circle(-radius)
    bob.penup()
    bob.forward(dia + extra)
    
turtle.done()