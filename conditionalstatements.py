# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:54:12 2021

@author: mehdi
"""
#assignment 3.1
"""3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
  Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
  Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
  You should use input to read a string and float() to convert the string to a number. 
  Do not worry about error checking the user input - assume the user types numbers properly."""
#my code    
hrs = input ("enter hours: ")
h = float(hrs)
rate = input ("enter rates: ")
r = float (rate)

if h < 40:
    gpay = h*r 
    print ("Gross pay", gpay)
else:
    gpay = 40.0*r + 1.5*r*(h - 40.0)# 45-40=5, 5 extra saat ücün rate hesablanir, bu zaman 40 üzeri oldugu ücün normal rate 1.5e vurulur, ve sonra da 5e ki extra saat ucun payi hesablayaq ve sonra onu normal saat ve rate ucun olan payla elave edek.
print ("Pay extra", gpay)
    
    
#teachers code
hrs = input ("enter hours: ")
h = float(hrs)
rate = input ("enter rate: ")
r = float (rate)

if h > 40:
    #print ("overtime")
    reg = 40.0*r #regular pay
    otp = (h - 40.0)*(r*1.5) #overtime pay
    #print("reg, otp")
    xp = reg + otp
else:
    #print("regular")
    xp = h*r
print("Pay:", xp)


#assignment 3.2
#same code with try/except structure
hrs = input ("enter hours: ")
rate = input ("enter rates: ")

try:
    h = float(hrs)
    r = float (rate) 
except:
    print("Error, please enter numeric input")
    quit() #if we don´t say quit here, we will get traceback in 54th line when try fails.
print(h, r) #when, e.g, try fails due to r, then this print function cannot run since the wrong input was entered by a user(like, not ´10´, but ´ten´, latter is a wrong input)
#so we have to say quit so it won´t continue on to run print(h,r)
if h < 40:
    gpay = h*r 
    print ("Gross pay", gpay)
else:
    gpay = 40.0*r + 1.5*r*(h - 40.0)
print("Pay extra", gpay) 

#assignment 3.3
score = input("Enter Score: ")
try:
    sgrade = float (score)
except: 
    print("please enter a number")
    quit()
if sgrade <= 0.0 or sgrade >= 1.0:
    print ("Please enter the value between 0.0 and 1.0")
elif sgrade >=0.9:
    print("A")

elif sgrade >=0.8:
    print("B") 

elif sgrade >=0.7:
    print("C")

elif sgrade >=0.6:
    print("D")

elif sgrade <0.6:
    print("F")

#else:
    #print ("error")



        