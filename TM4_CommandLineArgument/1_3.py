# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 13:36:34 2021

@author: UDITYA SARAF
"""

import sys

nums = sys.argv


def with_loop():
    total = 0   
    count = 1  
    for i in range(10):
        num = int(input("{}. Please enter a number: ".format(count)))
        if num > 1:  
            for j in range(2, num):
                if (num % j) == 0:
                    break
            else:
                total += num
        elif num == 1:   
            total += num
        else:   
            pass
        count += 1
    print("\nTotal : {}".format(total))

with_loop()
