# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:41:41 2021

@author: UDITYA SARAF
"""

file1 = open('DemoFile.txt','w')

n = input("Enter any content:-")

file1.write(n)

file1.close()