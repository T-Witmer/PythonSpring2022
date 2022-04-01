#Troy Witmer

import random



def rolld6():
    return random.randint(1,6)

def turnss():
    score = input("Turns? ")
    while score.isnumeric() == False:
        score = input("Turns? ")
    return int(score)
def hold():
    score = input("Holdvalue? ")
    while score.isnumeric() == False:
        score = input("Holdvalue? ")
    return int(score)

def part1():
    turnScore = 0
    done = False
    while not done:
        result = rolld6()
        #print("Roll:",result)
        if result == 1:
            turnScore = 0
            done = True
        else:
            turnScore = turnScore + result
            if turnScore >= 20:
                done = True
    #print("Turn Score:", turnScore)
    
    
    return turnScore

def part1demo():
    turnScore = 0
    done = False
    while not done:
        result = rolld6()
        print("Roll:",result)
        if result == 1:
            turnScore = 0
            done = True
        else:
            turnScore = turnScore + result
            if turnScore >= 20:
                done = True
    print("Turn Score:", turnScore)

def part2():
    turns = turnss()
    outcomes = {}
    outcomes[0] = 0
    for score in range(20,26):
        outcomes[score] = 0
    for _ in range(turns):
        turnScore = part1()
        outcomes[turnScore] += 1
    print("Score\tProbability")
    for score in outcomes:
        print(score,str(outcomes[score]/turns*100)+"%",sep="\t")


def holdAtXTurn(holdValue):
    turnScore = 0
    done = False
    while not done:
        result = rolld6()
        #print("Roll:",result)
        if result == 1:
            turnScore = 0
            done = True
        else:
            turnScore = turnScore + result
            if turnScore >= holdValue:
                done = True
    #print("Turn Score:", turnScore)
    return turnScore



def part3():
    turns = turnss()
    holdValue = hold()
    outcomes = {}
    outcomes[0] = 0
    for score in range(holdValue,holdValue+6):
        outcomes[score] = 0

    for _ in range(turns):
        turnScore = holdAtXTurn(holdValue)
        outcomes[turnScore] += 1
    print("Score\tProbability")
    for score in outcomes:
        print(score,str(outcomes[score]/turns*100)+"%",sep="\t")

#part3(100000,100)
def score():
    score = input("Score? ")
    while score.isnumeric() == False:
        score = input("Score? ")
    return int(score)

def part4demo():
    score = int(input("Score? "))
    turnScore = 0
    done = False
    while not done:
        result = rolld6()
        print("Roll:",result)
        if result == 1:
            score -= turnScore
            turnScore = 0
            done = True
        else:
            turnScore += result
            if turnScore >= 20 or result + score >= 100:
                done = True
            score += result
    print("Turn Score: ", turnScore)
    print("Total Score: ", score)
    
    return turnScore

def part4(score):
    #score = int(input("Score? "))
    turnScore = 0
    done = False
    while not done:
        result = rolld6()
        #print("Roll:",result)
        if result == 1:
            score -= turnScore
            turnScore = 0
            done = True
        else:
            turnScore += result
            if turnScore >= 20 or result + score >= 100:
                done = True
            score += result
    #print("Turn Score: ", turnScore)
    #print("Total Score: ", score)
    
    return turnScore

def part4demo5(score):
    #score = int(input("Score? "))
    turnScore = 0
    done = False
    while not done:
        result = rolld6()
        print("Roll:",result)
        if result == 1:
            score -= turnScore
            turnScore = 0
            done = True
        else:
            turnScore += result
            if turnScore >= 20 or result + score >= 100:
                done = True
            score += result
    print("Turn Score: ", turnScore)
    print("Total Score: ", score)
    
    return turnScore

def part5():
    total = 0
    turns = 0
    while total <= 100:
        total += part4demo5(total)
        turns += 1
    return turns, total

def part56():
    total = 0
    turns = 0
    while total <= 100:
        total += part4(total)
        turns += 1
    return turns, total

def part6():
    games = int(input("Games? "))
    outcomes = {}
    outcomes[0] = 0
    total = 0
    for game in range(games):
        outcomes[game] = 0
    for i in outcomes:
        outcomes[i] = part56()[0]
    for i in outcomes:
        total += outcomes[i]
    average = total/games
    print("Average Turns: ", average)
    return average

def playerinput():
    x = input("Leave blank to roll, type anything to hold: ")
    return x

def part7():
    player1score = 0
    player2score = 0
    player1turn = True
    while player1score <= 100 or player2score <= 100:
        print("Player 1 score: ", player1score)
        print("PLayer 2 score: ", player2score)
        turnScore = 0
        print("it is player 1's turn")
        while player1turn is True:
            result = rolld6()
            print("Roll: ", result)
            if result == 1:
                player1score -= turnScore
                turnScore = 0
                player1turn = False
            else:
                turnScore += result
                if turnScore >= 20 or result + player1score >= 100:
                    player1turn = False
                player1score += result
        print("Turn Score: ", turnScore)
        print("Player1 NewScore: ", player1score)
        print("")
        if player1score >= 100:
            print("Player 1 score: ", player1score)
            print("PLayer 2 score: ", player2score)
            print("")
            print("Player 1 wins! ")
            break
        print("it is player 2's turn")
        turnScore = 0
        while player1turn is False:
            result = rolld6()
            print("Roll: ", result)
            if result == 1:
                player2score -= turnScore
                turnScore = 0
                player1turn = True
            else:
                turnScore += result
                if turnScore >= 20 or result + player2score >= 100:
                    player1turn = True
                player2score += result
            
        print("Turn Score: ", turnScore)
        print("Player2 NewScore: ", player2score)
        print("")
        if player2score >= 100:
            print("Player 1 score: ", player1score)
            print("PLayer 2 score: ", player2score)
            print("")
            print("Player 2 wins! ")
            break  

def part8():
    player1score = 0
    player2score = 0
    turn = random.randint(1,2)
    if turn == 1:
        player1turn = True
    else:
        player1turn = False
    
    while player1score <= 100 or player2score <= 100:
        print("Player 1 score: ", player1score)
        print("Computer's score: ", player2score)
        turnScore = 0
        print("it is player 1's turn")
        while player1turn is True:
            decision = playerinput()
            if decision == "":
                result = rolld6()
                print("Roll:",result)
            elif decision is not "":
                player1turn = False
            if result == 1:
                player1score -= turnScore
                turnScore = 0
                player1turn = False
            else:
                turnScore += result
                if result + player1score >= 100:
                    player1turn = False
                player1score += result
        print("Turn Score: ", turnScore)
        print("Player1 NewScore: ", player1score)
        print("")
        if player1score >= 100:
            print("Player 1 score: ", player1score)
            print("Computer's score: ", player2score)
            print("")
            print("Player 1 wins! ")
            break
        print("it is the Computer's turn")
        turnScore = 0
        while player1turn is False:
            result = rolld6()
            print("Roll:",result)
            if result == 1:
                player2score -= turnScore
                turnScore = 0
                player1turn = True
            else:
                turnScore += result
                if turnScore >= 20 or result + player2score >= 100:
                    player1turn = True
                player2score += result
            
        print("Turn Score: ", turnScore)
        print("Computer's NewScore: ", player2score)
        print("")
        if player2score >= 100:
            print("Player 1 score: ", player1score)
            print("Computer's score: ", player2score)
            print("")
            print("Computer wins! ")
            break  

def part9():
    player1score = 0
    player2score = 0
    player1turn = True
    while player1score <= 100 or player2score <= 100:
        print("Player 1 score: ", player1score)
        print("PLayer 2 score: ", player2score)
        turnScore = 0
        print("it is player 1's turn")
        while player1turn is True:
            decision = playerinput()
            if decision == "":
                result = rolld6()
                print("Roll:",result)
            elif decision is not "":
                player1turn = False
            if result == 1:
                player1score -= turnScore
                turnScore = 0
                player1turn = False
            else:
                turnScore += result
                if result + player1score >= 100:
                    player1turn = False
                player1score += result
        print("Turn Score: ", turnScore)
        print("Player1 NewScore: ", player1score)
        print("")
        if player1score >= 100:
            print("Player 1 score: ", player1score)
            print("PLayer 2 score: ", player2score)
            print("")
            print("Player 1 wins! ")
            break
        print("it is player 2's turn")
        turnScore = 0
        while player1turn is False:
            decision = playerinput()
            if decision == "":
                result = rolld6()
                print("Roll:",result)
            elif decision is not "":
                player1turn = True
            if result == 1:
                player2score -= turnScore
                turnScore = 0
                player1turn = True
            else:
                turnScore += result
                if result + player2score >= 100:
                    player1turn = True
                player2score += result
            
        print("Turn Score: ", turnScore)
        print("Player2 NewScore: ", player2score)
        print("")
        if player2score >= 100:
            print("Player 1 score: ", player1score)
            print("PLayer 2 score: ", player2score)
            print("")
            print("Player 2 wins! ")
            break  

def game():
    done = False
    while not done:
        game = input("what game do you want to play? \n part1 => 1 \n part2 => 2 \n part3 => 3 \n part4 => 4 \n part5 => 5 \n part6 => 6 \n part7 => 7 \n part8 => 8 \n part9 => 9 \n Enter: ")
        while game.isnumeric() == False and game not in "123456789":
            game = input("what game do you want to play? \n part1 => 1 \n part2 => 2 \n part3 => 3 \n part4 => 4 \n part5 => 5 \n part6 => 6 \n part7 => 7 \n part8 => 8 \n part9 => 9 \n Enter: ")
        if game == "1":
            part1demo()
        elif game == "2":
            part2()
        elif game == "3":
            part3()
        elif game == "4":
            part4demo()
        elif game == "5":
            part5()
        elif game == "6":
            part6()
        elif game == "7":
            part7()
        elif game == "8":
            part8()
        elif game == "9":
            part9()
        elif game == "":
            done = True

game()
#part4(score())
#part5()
#part6()