# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 13:02:36 2021

@author: UDITYA SARAF
"""

my_dict = {}

x = int(input("Enter number of items to add"))

for x in range(0,x):
    #for y in range(1,15):
        y = str(input("Key : "))
        z = str(input("Value : "))
        my_dict.update({y:z})
      
print(my_dict)

for y in my_dict:
    print(y)
    
for y in my_dict:
    print(my_dict[y])

    
    
    