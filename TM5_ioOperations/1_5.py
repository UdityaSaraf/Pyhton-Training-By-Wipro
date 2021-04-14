# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:33:22 2021

@author: UDITYA SARAF
"""

def longestWord(file1):
    with open(file1, 'r') as infile:
              chars = infile.read().split()
    max_len = len(max(chars, key=len))
    return [char for char in chars if len(char) == max_len]

print(longestWord('DemoFile.txt'))
