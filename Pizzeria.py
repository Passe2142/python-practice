# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:40:42 2021

@author: Jules
"""


# Game


pizza = str(input("Choose your pizza, Small, Medium or Large: "))

if pizza == "Small":
    bill = 15
    
elif pizza == "Medium":
    bill = 20


elif pizza == "Large":
    bill = 25

else:
    print("Choose a proper pizza size.")
    
extraCheese = input("With extra cheese? Y or N: ")
pepperoni = input("With pepperoni? Y or N: ")

if pepperoni == "Y":
    if pizza == "Small":
        bill +=2
    else: 
        bill +=3
if extraCheese == "Y":
    bill += 1
    
print(f"Your bill is {bill}$.")
