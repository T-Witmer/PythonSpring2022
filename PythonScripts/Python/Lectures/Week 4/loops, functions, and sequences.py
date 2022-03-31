#Troy Witmer

import turtle

for i in range(5):
    print(i)

text = "日本語"
for char in text:
    print(char)

print(ord("日"))   #Prints order
 #Prints Character

low = [2,4,-8,-7,-2,-7,-2,3,4,-2] #List Sequence

total = 0
for temp in low:
    total = total + temp

print(total)
print(len(low))
print(total / len(low))

print(len(text))


bob = turtle.Turtle()
bob.pensize(3)
'''
bob.speed(0)
colors = ["red","blue","green","yellow","black","pink"]

for i in range(20):
    for color in colors:
        bob.color(color)
        bob.forward(100)
        bob.right(87)

turtle.done()
'''
def shoutIt(text):                #DEFINES A NEW FUNCTION
    SHOUTY_TEXT = text.upper()
    print(SHOUTY_TEXT)

shoutIt("hello")

def sayhi():
    print("hi")

def drawSquare(T,size):
    for i in range(4):
        T.forward(size)
        T.left(90)

#drawSquare(bob,50)

#turtle.done()

'''
for i in range(10):
    bob.color(0+i*.1 , 0 , 1-i*.1)
    drawSquare(bob,100)
    bob.forward(10)
'''
bob.speed(0)
for i in range(13):
    bob.color(0+i*.07 , 0 , 1-i*.07)
    drawSquare(bob,100)
    bob.forward(300)
    bob.left(60)
    for i in range(10):
        bob.color(0+i*.07 , 0 , 1-i*.07)
        drawSquare(bob,100)
        bob.forward(20)
        bob.left(20)



turtle.done()