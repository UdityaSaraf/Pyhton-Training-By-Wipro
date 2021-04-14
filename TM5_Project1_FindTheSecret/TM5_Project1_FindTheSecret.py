# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:58:05 2021

@author: UDITYA SARAF
"""

file1 = open("projectdoc.txt","r")

#Hours logic
line_count = 0
for line in file1:
    if line != "\n":
        line_count += 1
    
if((line_count >= 1) and (line_count <= 12)):
        print("Meeting time:-", line_count,("AM"))
if((line_count > 12) and (line_count <=24)):
        print("Meeting time:-", line_count-12,("PM"))


#place logic
count = 0;  
word = "";  
maxCount = 0;  
words = [];  
   
file1 = open("projectdoc.txt", "r")  
      
for line in file1:  
    string = line.lower().replace(',','').replace('.','').split(" ");  
    for s in string:  
        words.append(s);  
   
for i in range(0, len(words)):  
    count = 1;  
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;  
              
    if(count > maxCount):  
        maxCount = count;  
        word = words[i];  
          
print("Meeting Place: " + word);  
file1.close()


















