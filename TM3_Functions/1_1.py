# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:54:19 2021

@author: UDITYA SARAF
"""
l = []

x = int(input("Enter elements in the list"))

for x in range(0,x):
    list = int(input())
    
    l.append(list)

print(l)

def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


total = sumOfList(l, len(l))

print("Sum of all elements in given list: ", total)
