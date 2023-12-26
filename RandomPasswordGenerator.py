# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 07:47:28 2021

@author: Jules
"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to password generator!")
nrLetters = int(input("How many letters would you like in your password? "))

nrSymbols = int(input("How many symbols would you like in your password? "))

nrNumbers = int(input("How many numbers would you like in your password? "))


    

passwordList = []

for char in range(0, nrLetters):
    passwordList.append(random.choice(letters))

for char in range(0, nrSymbols):
    passwordList.append(random.choice(symbols))

for char in range(0, nrNumbers):
    passwordList.append(random.choice(numbers))

random.shuffle(passwordList)

password = ""
for char in passwordList:
    password += char

print(f"Your password is {password}!")
    

