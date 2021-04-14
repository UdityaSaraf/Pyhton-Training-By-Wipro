# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
  
l1 = []

x = int(input("Enter the number of elements in the list"))

for i in range(0,x):
    my_list = int(input())
    
    l1.append(my_list)

print(l1)

x  = int(input("Remove the element in the list from index:- "))

del l1[x]

print(l1)