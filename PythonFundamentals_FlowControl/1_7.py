# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lower = 10  
upper = 99
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num," is a prime number")  

        
    