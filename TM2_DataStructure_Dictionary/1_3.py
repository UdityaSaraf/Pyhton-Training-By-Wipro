# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 12:29:15 2021

@author: UDITYA SARAF
"""

my_dict = {}

x = int(input("Enter number of items to add"))

for x in range(0,x):
    y = int(input("Key : "))
    z = int(input("Value : "))
    my_dict.update({y:z}) 
print(my_dict)

a = int(input("Enter the key you want to check "))

if a in my_dict:
    print("Yes", a , "is present in the dictionary")
    print("Value of the key is:- ", my_dict[a])
else:   
    print("Key not present")

