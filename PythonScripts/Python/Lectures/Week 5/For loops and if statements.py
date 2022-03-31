


loan_amount = [1250.0, 500.0, 1450.0, 200.0, 700.0, 100.0, 250.0, 225.0, 1200.0, 150.0, 600.0, 300.0, 700.0, 125.0, 650.0, 175.0, 1800.0, 1525.0, 575.0, 700.0, 1450.0, 400.0, 200.0, 1000.0, 350.0]

country_name = ['Azerbaijan', 'El Salvador', 'Bolivia', 'Paraguay', 'El Salvador', 'Philippines', 'Philippines', 'Nicaragua', 'Guatemala', 'Philippines', 'Paraguay', 'Philippines', 'Bolivia', 'Philippines', 'Philippines', 'Madagascar', 'Georgia', 'Uganda', 'Kenya', 'Tajikistan', 'Jordan', 'Kenya', 'Philippines', 'Ecuador', 'Kenya']

time_to_raise = [193075.0, 1157108.0, 1552939.0, 244945.0, 238797.0, 1248909.0, 773599.0, 116181.0, 2288095.0, 51668.0, 26717.0, 48030.0, 1839190.0, 71117.0, 580401.0, 800427.0, 1156218.0, 1166045.0, 2924705.0, 470622.0, 24078.0, 260044.0, 445938.0, 201408.0, 2370450.0]

num_lenders_total = [38, 18, 51, 3, 21, 1, 10, 8, 42, 1, 18, 6, 28, 5, 16, 7, 54, 1, 18, 22, 36, 12, 8, 24, 8]

min_loan = min(loan_amount)
max_loan = max(loan_amount)

targetmin = loan_amount.index(min_loan)
targetmax = loan_amount.index(max_loan)

min_country = country_name[targetmin]
max_country = country_name[targetmax]

# Your code here
'''
p_total = 0
index_lst = [5, 6, 9, 11, 13, 14, 22]
for index in index_lst:
    p_total += loan_amount[index]

p_average = p_total / len(index_lst)
'''

p_total = 0
p_count = 0
'''
for i in range(len(country_name)):
    name = country_name[i]
    if name == "Philippines":
        p_total += loan_amount[i]
        p_count += 1
p_average = p_total / p_count

print(p_average)
'''
'''
for index,name in enumerate(country_name):
    print(index,name)
    if name == "Philippines":
        p_total += loan_amount[index]
        p_count += 1
p_average = p_total / p_count

print(p_average)
'''
'''
for name,amount in zip(country_name,loan_amount):
    print(name,amount)
    if name == "Philippines":
        p_total += amount
        p_count += 1
p_average = p_total / p_count

print(p_average)
'''

for char in "hello":
    print(char)

for i in range(0,10):
    print(i**2)
#creates list of numerical numbers

#used mostly for index operations


word = "hello"
for index in range(len(word)):
    print("the letter at index", index, "is", word[index])

#prints out the position anf what is at the position in the index

# The accumulator pattern:

numLenders = [1,45,4,3,22,6,765,4,554,3,44,90,12,3,3,44,90]
total = 0

for value in numLenders:
    total += value

print(total)

#same as above:
print(sum(numLenders))

#step by step how it works
numLenders = [1,45,4,3,22,6,765,4,554,3,44,90,12,3,3,44,90]
total = 0

for value in numLenders:
    print("Current total is", total, "\t reading", value, "\t Updating total to", total + value)
    total += value

print(total)
 # Its an amazing tool that we will use a lot of

#finding averages
total = 0

for value in numLenders:
    total += value

average = total / len(numLenders)
print(average)

# Traversal

fruits = ["apple","banana","pear","grape","apple","grape"]

for n in range(len(fruits)):
    print(n, fruits[n])

# Using enumerate
total = 0

for i,name in enumerate(fruits):
    print(i, name)
    if name == "apple":
        total += 1

print(total)




