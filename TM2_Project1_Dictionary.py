# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 00:06:59 2021

@author: UDITYA SARAF
"""

my_dict = {}

x = int(input("Enter number of people to add"))

for x in range(0,x):
    y = str(input("Person : "))
    z = str(input("Fact : "))
    my_dict.update({y:z}) 
print(my_dict)

y = str(input("Change of fact for any Person:- "))

#y = str(input("Key : "))
z = str(input("New fact : "))
my_dict.update({y:z})

print(my_dict)


y = str(input("Enter new Person to add : "))
z = str(input("Enter new fact for the person : "))

my_dict.update({y:z})
print(my_dict)


