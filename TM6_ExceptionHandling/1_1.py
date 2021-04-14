# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:15:17 2021

@author: UDITYA SARAF
"""

try:
    num = float(input("Enter numerator:-"))
    dem = float(input("Enter denominator:-"))
    result = num/dem
        
except ZeroDivisionError:
    print("ERROR- Denominator can't be 'Zero'")

else:
    print(result)
