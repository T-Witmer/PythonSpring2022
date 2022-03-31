#Troy Witmer

doubleVowels = {"ei": "ay", "ai": "eye","ae" : "eye", "ao": "ow", "au":"ow", "eu": "eh-oo", "iu": "ew", "oi": "oyo", "ou": "ow", "ui": "ooey"}
vowels = {"a" : "ah" , "i" : "ee", "e" : "eh", "o": "oh", "u": "oo"}
consonants = ["h" , "w" , "k", "p", "l", "m", "n",]

def validate(word):
    word = word.lower()
    counter = 0
    for i in range(len(word)):
        if word[i] in " 'aiehwkplmnou":
            counter += 1
        else:
            invalid = word[i]
            counter += 0
    if counter == len(word):
        return True
    else:
        print(invalid, "is not a Hawaiian character")
        return False

def pronounce(word):
    word = word.lower()
    output = ""
    index = 0
    while index < len(word):
        if word[index: index + 2] in doubleVowels:
            output += doubleVowels[word[index: index + 2]]
            index += 2

        elif word[index] in vowels:
            output += vowels[word[index]]
            index += 1
            
        elif word[index] in consonants:
            if word[index] == "w":
                if index == 0:
                    output += "w"
                elif word[index - 1] == "a":
                    output += "w"
                    
                elif word[index - 1] in "ie":
                    output += "v"
                    
                elif word[index - 1] in "uo":
                    output += "w"
                index += 1

            else:   
                output += word[index]
                index += 1
        elif word[index] == " ":
            output = output.strip("-")
            output += " "
            index += 1

        elif word[index] == "'":
            output = output.strip("-")
            output += "'"
            index += 1

        if index >= len(word) or word[index-1] == "'" or word[index-1] == " " or word[index-1] in consonants:
            output += ""
        else:
            output += "-"    

    return output.capitalize()

def another():
    answer = input("Do you want to enter another word? [YES/Y/NO/N] ==> ")
    if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
            return True
    elif answer == "n" or answer == "N" or answer == "no" or answer == "NO":
            return False
    while answer not in "yesnoYESNO":
        answer = input("Enter Y / YES / N / NO==> ")
        if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
            return True
        elif answer == "n" or answer == "N" or answer == "no" or answer == "NO":
            return False

def program():
    word = input("Enter a Hawaiian word to pronounce ==> ")
    while not validate(word):
        word = input("Enter a Hawaiian word to pronounce ==> ")
    print(word, "is pronounced", pronounce(word))
    while another() == True:
        word = input("Enter a Hawaiian word to pronounce ==> ")
        while not validate(word):
            word = input("Enter a Hawaiian word to pronounce ==> ")
        print(word, "is pronounced", pronounce(word))
        print("")
        

program()

# keiki
