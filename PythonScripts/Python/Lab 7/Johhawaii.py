doubleVowels = {"ei": "ay" , "ai": "aye", "ao": "ow", "au": "ow", "eu": "eh-oo", "iu": "ew", "oi": "oyo", "ou": "ow", "ui": "ooey"}
vowels = {"a": "ah", "i":"ee", "e": "eh", "o": "oh", "u": "oo"} 
consonants = {"l": "l", "m":"m", "n": "n", "h": "h", "p": "p", "k": "k", "w":"w", "aw": "aw", "iw": "v", "ew": "v", "uw": "w", "ow": "w"}
validChar = {" ", "'", "a", "e", "i", "o", "u", "p", "k", "h", "l", "m", "n", "w"}
invalid = ""


def validate(wordList): 
    #Validates that the word contains valid characters 
    global invalid 
    for element in wordList:
        if element not in validChar:
            invalid = element + " "
            return False
    return True


def pronounce(word):
            # get pronunciation of letter from the dictionary 
            # add that value to the output 
            # add a dash to the output 
    word = word.lower()
    output = []
    outputString = ""
    index = 0 
    while index < len(word):
        if word[index:index+2] in doubleVowels:
            output.append(doubleVowels.get(word[index:index+2]) + "-")
            outputString = "".join(output)
            index += 2 
            pass
        elif word[index] in vowels:
            output.append(vowels.get(word[index]) + "-")
            outputString = "".join(output)
            index += 1 
            pass
        
        elif word[index] in consonants:
            if word[index] == "w":
                if index == 0:
                    output.append("w")
                elif word[index - 1] == "a":
                    output.append("w")
                elif word[index - 1] in "ie":
                    output.append("v")   
                elif word[index - 1] in "ou":
                    output.append("w")
            elif word[index]:
                    output.append(consonants.get(word[index]))
             
            outputString = "".join(output)
            index += 1 
            pass


        elif word[index] == " ":
            if output[-1][-1] == "-":
                output[-1] = output[-1][:-1]
            output.append(" ")
            index += 1
            
        elif word[index] == "'":
            if output[-1][-1] == "-":
                output[-1] = output[-1][:-1]
            output.append("'")
            index += 1
            
    if outputString[-1] == "-":
        outputString = outputString[:-1]
       
    print(word.upper(), " is pronounced ", outputString.capitalize())

def another():
    another = input("Do you want to enter another word? Y/YES/N/NO ==>")
    if another.upper() == "N" or another.upper() == "NO":
        return False
    if another.upper() == "YES" or another.upper() == "Y":
        return True
    while another not in "yyesYESYnoNOnN":
        another = input("Please enter Y/YES or N/NO==> " )
        if another.upper() == "N" or another.upper() == "NO":
            return False
        if another.upper() == "YES" or another.upper() == "Y":
            return True

while True: 
    word = input("Enter a hawaiian word to pronounce ==> ")
    lower = word.lower()
    #convert to a list
    wordList = list(word.lower())
    if validate(wordList):
        pronounce(word)    
    else:
        print("Sorry, ", invalid.upper(),"is an invalid character.")
    if another() == False:
        break






