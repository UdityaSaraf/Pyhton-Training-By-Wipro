# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:25:22 2021

@author: UDITYA SARAF
"""

try:
    num = int(input("Enter any number"))
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
                print(num, "is a prime number")
        
    else:
        print(num, "is not a prime number")

except ValueError:
        print("Error Occured")
        print("Don't give a char value")