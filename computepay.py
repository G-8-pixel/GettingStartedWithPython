# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:13:18 2021

@author: mehdi
"""

"""
 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
 Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
 Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
 The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
 You should use input to read a string and float() to convert the string to a number. 
 Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
 Do not name your variable sum or use the sum() function.
"""


def computepay(h,r):  
    if h < 40:
        gpay = h*r
        #print("Pay", gpay)
    else:
        gpay = 40.0*r + 1.5*(h - 40.0)*r
        #print("Pay", gpay)
    return gpay #defined functiondaki hesablamalarin neticesini return edir ki, call olunan zaman ashagidaki kod neticeni print ede bilsin, cunki def hecne print etmir.

hrs = input ("enter hours: ")
rate = input("enter rate: ")
try:
    h = float (hrs)
    r = float (rate)
except: 
    print("please enter a number")
    quit() 
#print(h,r)
p = computepay(h, r)
print ("Pay", p)