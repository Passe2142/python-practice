# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:52:29 2021

@author: Jules
"""
import random
import wordList
import HangManArt
chosenWord = random.choice(wordList.word_list)
chosenWordLen = len(chosenWord) 

display = []
for _ in range(chosenWordLen):
    display += "_"

print(HangManArt.logo)

endOfGame = False
lives = 6

while not endOfGame and lives > 0:
    guess = str(input("Guess a letter: ").lower())
    print(f"You have {lives} lives.")
    
    for position in range(chosenWordLen):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
      
    print(f"{' '.join(display)}")   
    
    if "_" not in display:
        endOfGame = True
        print("You win!.")        
    if guess not in chosenWord:
        print(f"The letter you guessed '{guess}', is not in the chosen word.")
        lives -= 1
        if lives == 0:
            endOfGame = True
            print(f"The word was {chosenWord}, you lose!.")
            
    print(HangManArt.stages[lives])
    
    
    
    
    
    