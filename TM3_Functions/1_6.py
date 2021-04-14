# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 01:52:00 2021

@author: UDITYA SARAF
"""

def prime_number(num):
   #num = int(input("enter a number"))
   if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
 
        else:
                print(num, "is not a prime number")
prime_number()        