# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:28:20 2021

@author: UDITYA SARAF
"""

def isPalindrome(s):
	for i in range(0, int(len(s)/2)):
		if s[i] != s[len(s)-i-1]:
			return ("Not a palindrome")
	return ("It is a palindrome")

