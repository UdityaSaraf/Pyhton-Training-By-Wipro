# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
my_dict = {}

x = int(input("Enter number of items to add"))

for x in range(0,x):
    y = input("Key : ")
    z = input("Value : ")
    my_dict.update({y:z}) 
print(my_dict)
