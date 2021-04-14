# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
  
l = []

x = int(input("Enter the range of list"))

for i in range(0,x):
    my_list = int(input())
    
    l.append(my_list)

print(l)

j = int(input("Enter the value you want to count")) 
my_list=l.count(j)
print(my_list)


index = int(input("Item to delete"))

l.remove(index)
print(l)