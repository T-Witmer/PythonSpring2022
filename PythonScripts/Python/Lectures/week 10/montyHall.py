# 3/22/2022

#monty Carlo simulations in textbook
#activity 11

import random

#what we need for a single game
def game(strategy):
    doors = ["goat","goat","car"] #whats behind the doors
    random.shuffle(doors) #shuffles the list randomly
    intitalChoice = doors[0] #always zero because statistically it doesnt matter
    if strategy == "stay":
        if doors[0] == "car":
            return True
        else:
            return False
    elif strategy == "switch":
        if doors[1] == "goat":
            revealed = doors[1]
            swap = doors[2]
        else:
            revealed = doors[2]
            swap = doors[1]
        if swap == "car":
            return True
        else:
            return False
        
trials = 5    #how many games
wins = 0       #counter for wins
strategy = "switch"
for i in range(trials):
    if game(strategy) == True:
        wins += 1
        
print("The Switch Strategy wins", wins, "out of", trials) 

#activity 1
#your code here
# recommend myturtle.tracer(12,25) for faster animation
import turtle
import random
import math
win = turtle.Screen()
win.setworldcoordinates(-1,-1,1,1)#sets world coors to a square with a side of 2 units
bob = turtle.Turtle()
bob.penup()
bob.speed(0)
bob.tracer(100,25)
bob.shape("arrow")
 
hits = 0
trials = 10000 #amoint of times we run the trial
for i in range(trials):
    x = random.uniform(-1,1) #unit circle with a radius of 1 units
    y = random.uniform(-1,1)
    bob.goto(x,y)
    distance = math.sqrt(x**2+y**2)
    if distance <= 1:
        bob.color("red")
        hits += 1
    else:
        bob.color("blue")
    bob.stamp()
bob.update()
print("pi =", (hits / trials)*4) #approx pi


