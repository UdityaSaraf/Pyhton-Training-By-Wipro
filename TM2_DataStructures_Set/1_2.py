# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:09:09 2021

@author: UDITYA SARAF
"""
s1 = set()
s2 = set()

x = int(input("How many elements you want"))

for i in range(0,x):
    set = int(input())
    
    s1.add(set)

print(s1)


x = int(input("How many elements you want"))

for i in range(0,x):
    set = int(input())
    
    s2.add(set)

print(s2)


print("Intersection of two sets :-", s2 & s1)


