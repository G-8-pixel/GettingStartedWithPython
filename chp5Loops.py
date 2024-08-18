# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:13:07 2021

@author: mehdi
"""

""" Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below."""
largest_num = None
smallest_num = None

while True:
    num = input ("enter a number: ")
    if num == "done":
        break
    try:
     inum = int (num) 
     
    #print (istr)
        
    except:
        print("Invalid input")
        continue
    else:
        if largest_num is None or inum > largest_num:
           largest_num = inum
        #elif inum > largest_num:
          # largest_num = inum
    #else:
        elif smallest_num is None or inum < smallest_num :
             smallest_num = inum
       # elif inum < smallest_num:
         #  smallest_num = inum
        print(largest_num, smallest_num)
            
print("Maximum is ", largest_num)
print("Minimum is ", smallest_num)
        
        
               
#CHAPTER5- LOOPS AND ITERATION; WHILE - indefinite loops; FOR - definite loops
#n = 5

m = input ("Enter a number: ")
n = int (m)

while n > 0:
    print(n)
    n = n - 1
print ("blastoff")
print(n) #residual value after the last iteration

while True:    # this loop continues until user enters the word "done"
    line = input ("> ")
    if line[0] == "#": # we use here continue bc we dont want to print a line with # as the first character [0].
        continue  # ends the current iteration and jumps to the top of the loop and starts the next iteration. 
    if line == "done":
        break #statement to get out of a loop, when the user enters "done", it get out of the loop and prints out DONE.
    print("line") # last line of this while loop block
print("DONE")

#Definite Loop: FOR

friends = ["Nigar", "Aygün", "Aysel"]
for friend in friends:
    print("Happy New Year", friend) 
    
#Finding the largest value

largest_so_far = -1  # before the loop we set the largest we´ve seen so far to -1 since we´ve seen nothing, we´ll see set of number in loop code. 
print("before", largest_so_far) 
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print (largest_so_far, the_num) 
print("after", largest_so_far) # after finishing all iterations; result should be 74, the largest.

#Finding the smallest value 
smallest = None # None means absence or lack of a value. So we say, before the loop starts, the smallest number we´ve seen is NOTING.
#So, None is foing to be our marker to indicate that we´ve seen no numbers
for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest is None: # first time, before starting loop, or going through number in the set.
        #if the smallest value is empty (None), there´s no value for smallest, then assign first number 9 in the set to the smallest. Then continue with next number in the set. 
        smallest = the_num
    elif the_num < smallest:
        smallest = the_num
    print (smallest, the_num) 
print("smallest", smallest) 

#Counting in a Loop
count = 0
print ("before", count)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    print(count, value)
print("after", count) #total number of items in the set

#Summing in a Loop
sum = 0
print ("before", sum)
for value in [9, 41, 12, 3, 74, 15]:
    sum = sum + value
    print(sum, value)
print("after", sum) #total sum of all the numbers in the set
average = int(sum / count) 
print (count, sum, average)

#Filtering in a loop
print("before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20: #using if in the loop to catch/filter the values we are looking for. In this case, we r looking for the values larger than 20
        print("large number", value) #prints out numbers larger than 20 in the set
print ("after")

#Search using a Boolean values: True, False
found = False
print("before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        #break #bc once it´s True it´s not going to back to False, so we could stop. 
    print (found, value)
print("after", found)

#Chapter5, exercises
"""Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count and average of the numbers. If the user enters anything other than a number, 
detect their mistake using try and except and print an error message and skip to the next number:"""

num = 0
tot = 0.0
while  True:
    sval = input("enter a number: ")   # string value
          

    if sval == "done":
        break # if user enter the word done, then break will work and code stop executing li´nes after these and go directly to the end and execute print (all done)
    try:
           fval = float(sval)                 # floating point value
           #print(fval)
    except:
           print("Please enter a number")
           continue
    num = num + 1    # counting the numbers
    tot = tot + fval # summing the numbers

print ("All Done")  
print(tot, num, tot/num)        

""" Write a program that prompts for a list of numbers as above and at the end prints out both 
the maximum and minimum of the numbers instead of the average"""

