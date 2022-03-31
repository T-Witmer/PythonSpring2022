#Troy Witmer

import turtle

wn = turtle.Screen()
def drawSquare(myTurtle, squareSize):
    for i in range(4):
        myTurtle.forward(squareSize)
        myTurtle.left(90)

def drawRow(myTurtle,length,squareSize):
    for i in range(1,length+1):
        drawSquare(myTurtle,squareSize)
        myTurtle.forward(squareSize)

def drawGrid(myTurtle,size,n):
    for i in range(1,size+1):
        drawRow(myTurtle,size,n)
        myTurtle.left(90)
        myTurtle.forward(n)
        myTurtle.left(90)
        myTurtle.forward(n*size)
        myTurtle.left(180)

def drawStairsleft(myTurtle, height, squareSize):
    for i in range(1,height+1):
        drawRow(myTurtle,height,squareSize)
        myTurtle.left(90)
        myTurtle.forward(squareSize)
        myTurtle.left(90)
        myTurtle.forward(squareSize*(height-1))
        myTurtle.left(180)
        height -= 1

def drawStairsright(myTurtle, height, squareSize):
    for i in range(1, height+1):
        drawRow(myTurtle, height, squareSize)
        myTurtle.left(90)
        myTurtle.forward(squareSize)
        myTurtle.left(90)
        myTurtle.forward(squareSize*height)
        myTurtle.left(180)
        height -= 1 

def drawNgon(myTurtle,numSides,sideLength):
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.left(360 / numSides)

def drawNgonSpiral(myTurtle,numSides,sideLength,numShapes):
    x = 360 // numShapes
    for _ in range(1,numShapes+1):
        myTurtle.color(0+_*(1/numShapes),0,1-_*(1/numShapes))
        drawNgon(myTurtle,numSides,sideLength)
        myTurtle.right(x)

def hourglass():
    print('|""""""""""|')
    for i in range(4,0,-1):
        for _ in range(5-i):
            print(" ",end="")
        print("\\", end=(""))
        for _ in range(0, 1*i):
            print(":", end=":")
        print("/", end=(""))
        print("")
    print("     ||")
    for i in range(1,5):
        for _ in range(5-i):
            print(" ",end="")
        print("/", end=(""))
        for _ in range(0, 1*i):
            print(":", end=":")
        print("\\", end=(""))
        print("")
    print('|""""""""""|')


def Art(n):
    for i in range(n):
        for _ in range(0+i):
            print("\\",end="\\")
        for _ in range(1,n-i):
            print("!",end="!")
        for _ in range(n-i):
            print("!",end="!")
        for _ in range(0+i):
            print("/",end="/")
        print("")


bob = turtle.Turtle()

bob.speed(0)

drawNgonSpiral(bob,6,100,36)

drawNgon(bob,6,100)
bob.clear()
bob.reset()
bob.speed(8)

drawSquare(bob,50)
bob.clear()
bob.reset()
bob.speed(8)

drawRow(bob,5,50)
bob.clear()
bob.reset()
bob.speed(8)

drawGrid(bob,5,50)
bob.clear()
bob.reset()
bob.speed(8)

drawStairsright(bob,5,50)

hourglass()

print("")

Art(4)

turtle.exitonclick()