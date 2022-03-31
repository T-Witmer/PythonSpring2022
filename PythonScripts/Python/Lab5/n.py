from tkinter import N


x = input("number: ")
while True:
    if x.isdigit() == True:
        n = x
        break
    else:
        x = input("try again: ")

