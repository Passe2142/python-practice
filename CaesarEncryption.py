# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 15:52:06 2021

@author: Jules
"""
import ArtCaesarCypher
print(ArtCaesarCypher.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, code, option):
    end_text = ""
    if option == "decode":
        code *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)        
            new_position = position + code
            end_text += alphabet[new_position]
        else:
            end_text += char        
    print(f"The option is {option} and text is {end_text}.")
    
answer = True
while answer:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26    
    caesar(message = text, code = shift, option = direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if result == "no":
        answer = False
