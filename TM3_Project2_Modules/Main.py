# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:03:21 2021

@author: UDITYA SARAF
"""

import palindrome 
import vowels
import charCount

s = str(input("Enter a string:-"))
x = palindrome.isPalindrome(s)


vow = "AaEeIiOoUu"
y = vowels.number_Vowels(s,vow)

z = charCount.charFrequency(s)

print(x)

print(y)

print(z)

