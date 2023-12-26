# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 06:08:03 2021

@author: Jules
"""
studentScores = input ("Input a list of students scores, ").split(",")


for n in range(0, len(studentScores)):
    studentScores[n] = int(studentScores[n])
print (studentScores)


studentScoresCounter = 0

maxScore = 0

maxScoreStudent = 0

for score in studentScores:
    if score > studentScores[n]:
        maxScore = score
        studentScoresCounter +=1
        maxScoreStudent = studentScoresCounter

print(f"The hightest score in the class is: {maxScore} and the student is {studentScoresCounter}.")