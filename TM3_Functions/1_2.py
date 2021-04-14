# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:25:05 2021

@author: UDITYA SARAF
"""

str1 = {}

x = str(input("Enter a string:- "))

def reverseString(x):
    return x[::-1]

str1 = reverseString(x)
print(str1)

