# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 07:38:40 2021

@author: Jules
"""
total = 0
for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
       print("Buzz")
    else:
        print(number)
        
        