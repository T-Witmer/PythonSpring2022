#Troy Witmer

n = int(input("How many bottles of beer? "))

for i in range(n):
    print(n, "bottles of beer on the wall", n, "bottles of beer\n"
        "Take one down pass it around", n-1, "bottles of beer on the wall")
    n -= 1