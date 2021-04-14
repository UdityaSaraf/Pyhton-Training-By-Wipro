# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
  
x=int(input("Enter the number "))  
revs_number = 0  
  
while (x > 0):  
      
    rem = x % 10  
    revs_number = (revs_number * 10) + rem  
    x = x // 10  
  
print(revs_number, "is reverse number")  



        
    