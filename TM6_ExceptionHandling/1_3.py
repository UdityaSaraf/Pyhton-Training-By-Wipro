# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 12:07:12 2021

@author: UDITYA SARAF
"""

try:
    file1 = open(input("Enter a file name:-"))

    print(file1.read())

    file1.close()

except:
    print("File Not found")
 