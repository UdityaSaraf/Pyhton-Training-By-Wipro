#-*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:43:12 2021

@author: UDITYA SARAF
"""

file_name = input("Enter the file name ")

f = open(file_name+".txt", "r")
lines = f.readlines()
if("(blank line)\n" in lines):
    lines.remove("(blank line)\n")  

no_of_items = len(lines)-1
no_of_free = 0
amount = 0
discount = 0

for i in range(len(lines)):
    lines[i] = lines[i].strip()  
    lines[i] = lines[i].split() 
    if(lines[i][1] == "Free"):
        no_of_free += 1
    elif(lines[i][0] == "Discount"):
        discount = int(lines[i][1])
    else:
        amount += int(lines[i][1])

print("No of items purchased:", no_of_items-no_of_free)
print("No of free items:", no_of_free)
print("Amount to pay:", amount)
print("Discount given:", discount)
print("Final amount paid:", amount-discount)
