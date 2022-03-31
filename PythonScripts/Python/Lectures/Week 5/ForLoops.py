# For loops

#for i in range(6):
	#print('hello')

# the variable can change value: 
#
#for i in range(6):
	#print(i)

# prints [0,6)
# 0 1 2 3 4 5

#range(2,5)
#prints[2,5)
# 2 3 4
"""
numTerms = 20


import math

den = 1
sign = 1
for i in range(numTerms):
	print(i, den + 2 * i, 1/(den + 2 * i), sign * 1/(den + 2 * i))
	sign = sign * -1

"""
'''
total = 0

for number in range(1,6):
	total += number

print(total)
'''

#Calculating pi

numTerms = 1000000000000000
total = 0
sign = 1

for i in range(numTerms):
	den = 1 + 2 * i
	term = sign / den
	total += term
	#print(i, den + 2 * i, 1/(den + 2 * i), sign * 1/(den + 2 * i))
	sign = sign * -1

print(total * 4)
