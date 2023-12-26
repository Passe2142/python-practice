# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 15:00:33 2021

@author: Jules
"""

year = int(input("Please enter a year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap!")
        else:
            print("Not Leap!")
    else:
        print("Leap!")
else:
    print("Not Leap!")

