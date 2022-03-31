# Chapter 6 Sequences
# 6.1 Introduction

# More complex data types
# 
# 6.2 Strings and Lists
# 
# Strings, used when working with words. creating string
#  empty stings "" , string with something in it "abcdefg"
#  concatonated stings "asd" + "kjh"
# 
notes = "asdkljfhqopweiru"
print(notes[3:5]) 

# .split cuts a sting up using a delimiter like a space
print(notes.split("k"))

# .index give first occurence  substring
print(notes.index("k"))

# .count gives amoutn  substring in string
print(notes.count("k"))

#List is a sequential collection  Python data values, where each is identified by an index
#Values that make up a list are called elements

notelist = [10, 20, 30, 40, 50, "Sixty"]
new = [.6, .5, .3]
#Append adds something to the end  the list
notelist.append("seventy")

#Add lists to combine them
newlist = notelist + new
print(newlist)

#This calls from list, elements in spaces 4,5 (indexing)
print(notelist[3:5]) 

# slicing cuts a list up, replaces what is in the index/spot of given list
newlist[3] = "changed this"
print(newlist)

# .index give first occurence elements in list
print(newlist.index(30))

# .count gives amount elements in list
print(newlist.count(30))

#Tuples
#cannot be changes like lists
#use () instead of []

julia = ("Julia", 1967 , 2009)

#Indexing Operator

school = "Luther College"
m = school[2]
print(m)

lastChar = school[-1]
print(lastChar)

#6.5 Lenght function

# len function when applied to a string returns the number of characters in a string
fruit = "banana"
print(len(fruit))

#To get the last letter in the string do

X = len(fruit)
last = fruit[X-1]
print(last)

#find the middle character

midchar = fruit[len(fruit)//2]
print(midchar)