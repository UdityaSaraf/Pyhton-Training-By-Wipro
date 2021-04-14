# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x= int(input("Enter a digit"))
sum = 0
while(x!=0):
    last = x%10
    sum = sum+last
    x = x//10
print(sum)


        
    