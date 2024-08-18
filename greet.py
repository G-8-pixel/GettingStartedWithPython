# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:06:14 2021

@author: mehdi
"""

#Chapter 4, store and reuse pattern, call function

def greet (lang):  # store part, def stores the greet function that we made and it´s code below. To run it we have to call the function.

    if lang == "es":    # lang is a parameter, es, fr and etc. are arguments of the function.
       print("Hola")
    if lang == "fr":
       print("Bonjour")
    else:
       print("Hallo")
    
x = greet ("fr")  # we call the function greet
print(x) 
#y = greet ("en")
#print(y)