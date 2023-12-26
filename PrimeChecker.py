# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 08:31:09 2021

@author: Jules
"""
def primeChecker(number):
    is_prime = True

    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

n =int(input("Insert a number: "))
 

primeChecker(number = n)
