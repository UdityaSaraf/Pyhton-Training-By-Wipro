# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:50:09 2021

@author: UDITYA SARAF
"""

with open('DemoFile.txt') as file1:
    content = file1.readlines()

line = [x.strip() for x in content]
print(line)

