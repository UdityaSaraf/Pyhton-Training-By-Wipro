# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:29:02 2021

@author: UDITYA SARAF
"""

s = set()

x = int(input("Enter elements in the set"))

for i in range(0,x):
    set = int(input())
    
    s.add(set)

print(s)


print("Maximum in the set:-", max(s))
print("Minimum in the set:-", min(s))