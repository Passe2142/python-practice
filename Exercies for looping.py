# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:55:47 2020

@author: Jules
"""
# Exercies for looping 

# 1) Print odds from 1 to 20

# Use a for loop aswell range 

# if and modulus to print out the odds

# 2) Round a float to 2 decimals

# 3) Demostrate compaund index

# Enter the user their interest investment amount and expeted interest

# Each year their investment will increase by their investment + investment * interest rate is

# Print out the earnings after a 10 year period


user_investment = float(input("Enter the amount that you would like to invest: "))

interest_rate = float(input("Enter interest rate: ")) * .01

# For example

for i in range(10):
    user_investment = user_investment + (interest_rate * user_investment)

print("The amount that increase in a ten year period: ", user_investment)


# While examples

import random

rand_num = random.randrange(1,51)

i = 1 

while i != rand_num:
    i += 1
    
print("The random values is: ", rand_num)


j = 1 
while j <= 20:
    if (j % 2) == 0:
        j += 1
        continue
        

    if j == 15:
        break
    print("Odds: ", j)
        
    j += 1
    

