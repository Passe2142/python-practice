# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 23:02:13 2021

@author: Jules
"""

import random

player = int(input("Player select a number, 0 is Rock, 1 is Paper and 2 is Sissors: "))

game = ['Rock', 'Paper', 'Sissors']

computer = game[random.randint(0, 2)]

if game[player] == computer:
    print(f"Player uses {game[player]} and Computer uses {computer}, its a draw!")

elif game[player] != computer and computer == "Paper":
    print(f"Player uses {game[player]} and Computer uses {computer}, Computer won!")

elif game[player] != computer and computer == "Rock":
    print(f"Player uses {game[player]} and Computer uses {computer}, Computer won!")

elif game[player] != computer and computer == "Sissors":
    print(f"Player uses {game[player]} and Computer uses {computer}, Computer won!")       

else:
    print(f"Player uses {game[player]} and Computer uses {computer}, Player won!")   





