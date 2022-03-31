#Troy Witmer

n = int(input("number for multiplication table "))

for i in range(1,n+1):
     print("")
     for _ in range(1,n+1):
          print(i * _ , end="\t") 