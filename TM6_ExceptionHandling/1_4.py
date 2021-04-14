# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 12:37:38 2021

@author: UDITYA SARAF
"""

try:
    list1 = [1,2,-3,4,5,-6,7,8,-9,10]
    index = int(input("Enter any index:-"))
    if(list1[index] > 0):
            print("Positive Number")
    elif(list1[index] < 0):
            print("Negative Number")
    else:
            print("Zero")
except IndexError:
    print("Invalid Index")
