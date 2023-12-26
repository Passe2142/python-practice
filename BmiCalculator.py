# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:33:18 2021

@author: Jules
"""

height = float(input("Please enter your height:")); weight = float(input("Please enter your weight:"))

bmi = round (weight / (height * height), 2); 

if bmi <= 18.5:
    print ("Underweight.")
elif bmi < 25:
    print ("Normal weight.")
elif bmi < 30:
    print ("Overweight.")
elif bmi < 35:
    print ("Obese.")
else: 
    print ("Clinically obese.")


print(f"BMI = {bmi} ")


