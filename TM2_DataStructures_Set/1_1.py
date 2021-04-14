# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:15:05 2021

@author: UDITYA SARAF
"""

s = set()

x = int(input("Enter elements in the set"))

for i in range(x):
    set = str(input())
    
    s.add(set)

print(s)

y = str(input("Enter element you want to remove"))
s.remove(y)
print(s)
