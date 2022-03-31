
import random
'''
#method 1
def Game1():
    cards = ["red","red","black","black","black","black","black"]
    random.shuffle(cards)
    draws = cards[:3]
    if "red" in draws:
        print("lose", draws, cards)
        return False
    else:
        print("win", draws, cards)
        return True
'''
'''
#method 2
def Game1():
    cards = ["red","red","black","black","black","black","black"]
    random.shuffle(cards)
    indexes = []
    while len(indexes) < 3:
        choice = random.randint(0,6)
        if choice not in indexes:
            indexes.append(choice)

    draws = []
    for i in indexes:
        draws.append(cards[i])

    if "red" in draws:
        print("lose", draws, cards)
        return False
    else:
        print("win", draws, cards)
        return True
'''
def Game1():
    cards = ["red","red","black","black","black","black","black"]
    random.shuffle(cards)
    draws = random.sample(cards,3)
    if "red" in draws:
        #print("lose", draws, cards)
        return False
    else:
        #print("win", draws, cards)
        return True

def Games(trials):
    wins = 0
    for i in range(trials):
        if Game1() == True:
            wins += 1
    ratio = wins/trials
    return wins, trials, ratio

print(Games(1))

def game2():
    deck = ["r"] * 2 + ["b"] * 7
    random.shuffle(deck)
    row0 = deck[0:3]
    row1 = deck[3:6]
    row2 = deck[6:9]
    grid = [row0,row1,row2]
    draws = []
    choice = random.randint(0,7)
    if choice == 0:
        draws = [grid[0][0], grid[0][1], grid[0][2]]
    elif choice == 1:
        draws = [grid[1][0], grid[1][1], grid[1][2]]
    elif choice == 2:
        draws = [grid[2][0], grid[2][1], grid[2][2]]
    elif choice == 3:
        draws = [grid[0][0],grid[1][0],grid[2][0]]
    elif choice == 4:
        draws = [grid[0][1],grid[1][1],grid[2][1]]
    elif choice == 5:
        draws = [grid[0][2],grid[1][2],grid[2][2]]
    elif choice == 6:
        draws = [grid[0][0],grid[1][1],grid[2][2]]
    elif choice == 7:
        draws = [grid[0][2],grid[1][1],grid[2][0]]
        
    if "r" in draws:
        #print("lose", draws, cards)
        return False
    else:
        #print("win", draws, cards)
        return True

def games2(trials):
    wins = 0
    for i in range(trials):
        if game2() == True:
            wins += 1
    ratio = wins/trials
    return wins, trials, ratio

print(games2(10000))