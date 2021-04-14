# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:46:48 2021

@author: UDITYA SARAF
"""


def number_Vowels(s, vow):
	final = [each for each in s if each in vow]
	return 'Vowels:-', len(final)



