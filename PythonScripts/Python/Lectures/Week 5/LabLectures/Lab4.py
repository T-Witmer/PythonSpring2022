#Troy Witmer

# printing tables

for row in range(1,5):
    for col in range(1,5):
        print('#', end=('\t'))
    print("")

# the hourglass:

for i in range(5,0,-1):
    for _ in range(6-i):
        print(" ", end="")
    for _ in range(0,1*i):
        print(i, end=" ")
    print("")
for i in range(1,6):
    for _ in range(6-i):
        print(" ", end="")
    for _ in range(0, 1*i):
        print(i, end=" ")
    print("")

