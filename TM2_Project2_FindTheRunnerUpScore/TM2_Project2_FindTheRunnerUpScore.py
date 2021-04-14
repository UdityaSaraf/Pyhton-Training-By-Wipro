# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:31:37 2021

@author: UDITYA SARAF
"""

l = []

#x = int(input())

for x in range(0,5):
    my_list = int(input())
    
    l.append(my_list)

print("Number of scores:-", l)

l.sort()

print("Runneer-Up score is:-", sorted(l)[-2])
