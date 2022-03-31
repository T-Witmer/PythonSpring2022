#Troy Witmer

date = input("enter date MM/DD/YYYY format:\n")

month = int(date[:2]) #splices month out of date
day = int(date[3:5])   #splices day out of date
year = int(date [6:])  #splices year out of date

# = ["", "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print(month, day, year)

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    if (day <= 31 and day > 0):
        print("Valid Date")
    else:
        print("Invalid Date, Invalid day")
elif (month == 4 or month == 6 or month == 9 or month == 11):
    if (day <= 30 and day > 0):
        print("Valid Date")
    else:
        print("Invalid Date, Invalid day")
elif (month == 2):
    if (day == 29):
        if (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    print("a leap year, Valid date")
                elif day > 29:
                    print("invalid date, Invalid day")
            else:
                print("not a leap year, Invalid date")
        else:
            print("not a leap year, Invalid date")
    elif(day < 29):
        print("Valid date")
    else:
        print("invalid date, invalid day")
else:
    print("Invalid month")
    

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    if (day <= 31 and day >0):
        print("Valid Date")
    else:
        print("Invalid date, Invalid day")
elif (month == 4 or month == 6 or month == 9 or month == 11):
    if (day <=30 and day >0):
        print("Valid Date")
    else:
        print("invalid date, Invalid Day")
elif (month == 2):
    if (day == 29):
        if isLeapYear(year) == True:
            print("A leap year, Valid date")
        else:
            print("Invalid date, not a leap year")
    elif (day < 29):
        print("valid date")
    else:
        print("invalid date, invalid day")
else:
    print("invalid date, invalid month")