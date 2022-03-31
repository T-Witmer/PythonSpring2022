#Troy Witmer


def height():
    while True:
        n = int(input("How tall do you want your pyramid? Please give us a number between 1 and 8: ")) 
        if n <=8 and n >=1:
            return n

n = height()
def mario():
    for i in range(n):
        for _ in range(n-(i-1)):
            print(" ", end="")
        for _ in range(1+i):
            print("#", end="")
        print("  ", end="")
        for _ in range(1+i):
            print("#", end="")
        print("")

        
mario()
