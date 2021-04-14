# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:39:40 2021

@author: UDITYA SARAF
"""

file1 = open('DemoFile.txt')

n = int(input("Enter number of lines you want to see:-"))

for i in range(0,n):
    line = file1.readline()
    print(line)

file1.close()