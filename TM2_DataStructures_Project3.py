# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:12:44 2021

@author: UDITYA SARAF
"""

n = int(input("Enter name and marks of students"))

student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Whose average percentage you want:- ")

print("Average Score is:- " +"{0:.2f}".format(round(sum(student_marks[query_name]) / len(student_marks[query_name]), 2)))



