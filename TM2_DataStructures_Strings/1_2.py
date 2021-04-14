# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:24:12 2021

@author: UDITYA SARAF
"""

string = str(input("Enter a string"))
flag = True

string = string.lower();

for x in range(0, len(string)//2):
      if(string[x] != string[len(string)-x-1]):  
        flag = False;  
        break;
   
if(flag):  
    print("String is palindrome");  
else:  
    print("String is not a palindrome");  