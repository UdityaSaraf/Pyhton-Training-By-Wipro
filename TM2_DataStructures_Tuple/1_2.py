
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:26:32 2021

@author: UDITYA SARAF
"""

tup = tuple(input("Enter Tuple"))

print("The tuple is:- ", tup)

check_item = input("Which element to check")
is_item_present = ("No")

for item in tup:
    if item == check_item:
        is_item_present = ("Yes")
        break
    
print('Is', check_item,'Present? ', is_item_present)
    
