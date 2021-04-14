# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
  

x = int(input("enter a number"))
 
temp = x
rev = 0
 
while temp != 0:
	rev = (rev * 10) + (temp % 10)
	temp = temp // 10
 
if x == rev:
	print(x," is palindrome")
else:
	print(x," is not palindrome")



        
    