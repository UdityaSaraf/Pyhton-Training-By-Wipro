# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 12:10:55 2021

@author: UDITYA SARAF
"""
my_dict = {}

my_dict1 = {}

x = int(input("Enter number of items to add in first dictionary:- "))

for x in range(0,x):
    y = input("Key : ")
    z = input("Value : ")
    my_dict1.update({y:z}) 
print(my_dict1)


my_dict2 = {}

x = int(input("Enter number of items to add in second dictionary:- "))

for x in range(0,x):
    y = input("Key : ")
    z = input("Value : ")
    my_dict2.update({y:z}) 
print(my_dict2)

my_dict3 = {}

x = int(input("Enter number of items to add in third dictionary:- "))

for x in range(0,x):
    y = input("Key : ")
    z = input("Value : ")
    my_dict3.update({y:z}) 
print(my_dict3)

my_dict.update(**my_dict1, **my_dict2, **my_dict3)
print(my_dict)

