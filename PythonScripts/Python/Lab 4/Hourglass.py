#Troy Witmer

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

n = int(input("number of rows: "))

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

hourglass()

