# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:41:36 2021

@author: UDITYA SARAF
"""

def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

num = int(input("Enter a number:- "))

if num < 0:
   print("Can't find factorial:- ")
elif num == 0:
   print("The factorial of 0 is 1:- ")
else:
   print("Factorial of", num, "is", factorial(num))    