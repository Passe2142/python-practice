# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:40:42 2021

@author: Jules
"""


# Love calculator

name = str(input("Please enter your full name: "))
crush = str(input("Please tell us your crush full name: "))

nameLowerCase = name.lower(); crushLowerCase = crush.lower()

lowerCaseCountTotalLove = nameLowerCase.count("t") + nameLowerCase.count("r") + nameLowerCase.count("u") + nameLowerCase.count("e") + crushLowerCase.count("t") + crushLowerCase.count("r") + crushLowerCase.count("u") + crushLowerCase.count("e")

lowerCaseCountTotalTrue = crushLowerCase.count("l") + crushLowerCase.count("o") + crushLowerCase.count("v") + crushLowerCase.count("e") + nameLowerCase.count("l") + nameLowerCase.count("o") + nameLowerCase.count("v") + nameLowerCase.count("e")


score = int(str(lowerCaseCountTotalLove) + str(lowerCaseCountTotalTrue))

if score < 10 or score > 90 :
    print(f"Your score is {score}%, you go toghether like coke and mentos." )
    

elif score >= 40 and score <= 50 :
        print(f"Your score is {score}%, you are alright toghether." )
            
else:
    print(f"Your score is {score}%." )

