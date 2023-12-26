# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:40:42 2021

@author: Jules
"""

tip1 = 0.1; tip2 = 0.12; tip3 = 0.15

messageA = "Welcome to tip calculator!"

print(messageA)

bill = float(input("What is your bill amount to pay? $")) 
people = float(input("How many people will split the bill? "))
tip = int(input("Please select the amount of percentage tip: 10, 12 and 15. "))


if tip == 10:
   a = round((bill + tip1 * bill) / people, 2)
   print(f"Each will pay: {a}$")
    
elif tip == 12:
    b = round((bill + tip2 * bill) / people, 2)
    print(f"Each will pay: {b}$")

elif tip == 15:
    c = round((bill + tip3 * bill) / people, 2)
    print(f"Each will pay: {c}$")
    
else:
    print("Please enter a valid tip.")
    










