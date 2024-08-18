# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:17:56 2021

@author: mehdi
"""

name = input ("your name:")
print ("Hello",name)

"""Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
You should use input to read a string and float() to convert the string to a number. """

hrs = float(input("Enter Hours:")) # or inputlar qalsin, multiplication olan lineda convert et

rate = float(input("Enter Rate:"))

pay = rate * hrs  # float(rate) * float(hrs)

print ("Pay:", pay)
