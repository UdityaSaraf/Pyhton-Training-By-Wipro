# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 13:51:59 2021

@author: UDITYA SARAF
"""

my_dict = {}

x = int(input("Enter number of items to add"))

for x in range(0,x):
    #for y in range(1,15):
        y = int(input("Key : "))
        z = int(input("Value : "))
        my_dict.update({y:z})
        
values = my_dict.values()

total = sum(values)

print(total)
print(my_dict)