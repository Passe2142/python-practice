# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:29:10 2021

@author: Jules
"""
import random
names = str(input("Please enter the names, "))

namesSplit = names.split(",")

print(f"{namesSplit[random.randint(0,(len(namesSplit)-1))]} is going to pay the meal today!")


#Choice function
print(f"{random.choice(namesSplit)} is going to pay the meal today!")


