# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 23:20:25 2021

@author: mehdi
"""

"""name = input("Enter file:")
handle = open (name)

counts = dict()
for line in handle:
     words = line.split()
     for word in words:
         counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)"""

#conditional statements
x = 5 
if x > 2:
    print ("bigger than 2")
    print ("still bigger")
print ("done with 2")

for i in range(5):
    print(i)
    if i > 2:
        print ("bigger than 2")
    print ("done with 2")
print ("all done")

#try/except structure: 
astr = input ("Enter a number: ") #try entering a number, and also any phrase to see how it works. 
try:
    ival = int(astr)  #we know that this int is dangerous since astr came from the user, whatever user typed. The user might entered not a number but something else, so using try/except here will help us to eliminate traceback...
except:
    ival = -1
if ival > 0:
    print ("nice work!")
else:
    print ("please enter a number")