# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 23:14:38 2021

@author: UDITYA SARAF
"""

l = []

x = int(input("Enter elements in the list"))

for x in range(0,x):
    list = int(input())
    l.append(list)
print(l)

def even(l,x):
    for x in range(0,1):
        l = [x for x in l if x%2==0]
        print("Even Numbers in the list:-", l)

even(l,x)

 












