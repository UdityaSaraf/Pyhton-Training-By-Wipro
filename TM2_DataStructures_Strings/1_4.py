# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:44:32 2021

@author: UDITYA SARAF
"""

string = str(input("Enter a string:- "))

if(string[0] == 'x' or string[-1] =='x'):
    print(string[1:len(string)-1])
else:
    print(string)
