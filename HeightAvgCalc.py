# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 06:23:41 2021

@author: Jules
"""

studentHeights = input ("Input a list of students heights, ").split(",")

for i in range(0, len(studentHeights)):
    studentHeights[i] = int(studentHeights[i])
print (studentHeights)    

total_height = 0 
for height in studentHeights:
    total_height += height 

numberOfStudents = 0
for student in studentHeights:
    numberOfStudents += 1

avg_height = total_height / numberOfStudents



print(f"The avg height is: {avg_height}.")


