# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:51:04 2021

@author: UDITYA SARAF
"""

def charFrequency(s):
    s = s.lower()
    dict = {}
    for char in s:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict