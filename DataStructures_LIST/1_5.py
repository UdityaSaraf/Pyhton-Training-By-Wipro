# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
  
l1 = []

x = int(input("Enter the range of first list"))

for i in range(0,x):
    my_list = int(input())
    
    l1.append(my_list)

print(l1)

l2 = []

x = int(input("Enter the range of second list"))

for i in range(0,x):
    my_list = int(input())
    
    l2.append(my_list)

print(l2)

print("Final List = ", l1 + l2)