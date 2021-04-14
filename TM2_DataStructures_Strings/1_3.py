# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:34:09 2021

@author: UDITYA SARAF
"""

string = str(input("Enter a string:- "))

if(len(string) >= 2):
    n = int(input("Number of copies you want:- "))
    print((string[0] + string[1])*n)

else:
    print("String is too short ")
    
    
    