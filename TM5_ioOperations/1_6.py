# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:46:10 2021

@author: UDITYA SARAF
"""

file1 = input("Enter file name: ")
word=input("Enter word to be searched:")
w = 0
 
with open(file1, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                w=w+1
print("Occurrences of the word:")
print(w)