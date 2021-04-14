# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 22:39:27 2021

@author: UDITYA SARAF
"""

def upper_lower():
    
    lower = 0
    upper = 0
    
    string = str(input("Enter any string:- "))
    
    for i in string:
        if (i.islower()):
            lower=lower+1
        elif (i.isupper()):
            upper=upper+1
    print("lower case letters:", lower)
    print("Upper case letters:", upper)
    
upper_lower()

