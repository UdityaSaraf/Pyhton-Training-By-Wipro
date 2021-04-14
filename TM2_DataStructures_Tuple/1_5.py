# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 20:36:17 2021

@author: UDITYA SARAF
"""
#Firt method:- Changing tuple into list.
x = tuple("Enter how many tuples you want")
#for tup in range(0,x):
tup1 = tuple(input("Enter first Tuple"))
tup2 = tuple(input("Enter second Tuple"))
tup3 = tuple(input("Enter third Tuple"))

#print("The tuple is:- ", tup1, tup2, tup3)
tup = tup1 + tup2 + tup3
print("The combined tuple is:- ", tup)

#Changing tuples into list

my_list1 = list(tup1)
my_list2 = list(tup2)
my_list3 = list(tup3)

#print(my_list1,my_list2,my_list3)


#giving last index value to 100 and changing list into tuples again
my_list1[-1] = '100'
tup1 = tuple(my_list1)

my_list2[-1] = '100'
tup2 = tuple(my_list2)

my_list3[-1] = '100'
tup3 = tuple(my_list3)

#printing updated index
print("Final tuple with last element as 100 :-", tup1, tup2, tup3)



#Second method using list as base.

'''
l = []

x = int(input("Enter Elements in the list"))

for x in range(0,x):
    list = int(input())
    
    l.append(list)

print(l)

tup = tuple(l)
print(tup)

l[-1] = '100'
tup = tuple(l)

print(tup)

'''







































