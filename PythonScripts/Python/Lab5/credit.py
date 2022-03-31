#Troy Witmer


n = input("Enter card number: ")
numlist = list(n)

#removing "-" if entered
for i in numlist:
    if i == "-":
        numlist.remove(i)

#Luhn Check
def creditcheck():
    for i in range(len(numlist)):
        numlist[i] = int(numlist[i])
    second_to_last = numlist[-2::-2]
    everything_else = numlist[-1::-2]

    for i in range(len(second_to_last)):
        second_to_last[i] = second_to_last[i] * 2
        if second_to_last[i] >= 10:    #If the product is 10 or greater than it will seperate the digits using append.
            second_to_last.append(second_to_last[i] % 10)
            second_to_last.append(second_to_last[i] // 10)
            second_to_last[i] = 0
            
    total = sum(second_to_last) + sum(everything_else)
    if total % 10 == 0:
        return True
    else:
        return False

def credit():
    if creditcheck() == True:
        if len(numlist) == 15:   #Check for 15 digit cards
            if numlist[0] == 3:
                if numlist[1] == 4 or numlist[1] == 7:
                    print("Number:",n, "\nAMERICAN EXPRESS")
            else:
                print("Number:",n, "\nPASSES CREDIT CHECK BUT NOT VISA, MASTERCARD, or AMERICAN EXPRESS")       

        elif len(numlist) == 16:    #Check for 16 digit cards
            if numlist[0] == 5:
                if numlist[1] == 1 or numlist[1] == 2 or numlist[1] == 3 or numlist[1] == 4 or numlist[1] == 5:
                    print("Number:",n,  "\nMASTERCARD")
            elif numlist[0] == 4:
                print("Number:",n, "\nVISA")
            else:
                print("Number:",n, "\nPASSES CREDIT CHECK BUT NOT VISA, MASTERCARD, or AMERICAN EXPRESS")

                        
        elif len(numlist) == 13:    #Check for 13 digit cards
            if numlist[0] == 4:
                print("Number:",n, "\nVISA")
        else:
                print("Number:",n, "\nPASSES CREDIT CHECK BUT NOT VISA, MASTERCARD, or AMERICAN EXPRESS")

    else:
        print("Number:",n, "\nINVALID")

credit()
