# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:16:00 2021

@author: UDITYA SARAF
"""

string = str(input("Enter a string: "))
upper=0
lower=0
for i in string:
    if (i.islower()):
        lower=lower+1
    elif (i.isupper()):
        upper=upper+1
print("lower case letters:",lower)
print("Upper case letters:",upper)