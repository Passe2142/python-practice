# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:05:32 2021

@author: Jules
"""

print('''
      _________________________________________________________
      ||-------------------------------------------------------||
      ||.--.    .-._                        .----.             ||
      |||==|____| |H|___            .---.___|""""|_____.--.___ ||
      |||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|---|||
      |||==|    | | |   | \         |   |   |_\/_|Black|  | ^ |||
      |||  |    | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ |||
      |||  |    | | |   |_\ \_( oo )|   |   |    |Magus|  | ^ |||
      |||==|====| |H|xxx|  \ \ |''| |+++|=-=|""""|-=+=-|==|---|||
      ||`--^----'-^-^---'   `-' ""  '---^---^----^-----^--^---^||
      ||-------------------------------------------------------||
      ||-------------------------------------------------------||
      ||               ___                   .-.__.-----. .---.||
      ||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||
      ||         ,  /(|   |_|III|__|''|__|:x:|=|  |     |=| Q |||
      ||      _a'{ / (|===|+|   |++|  |==|   | |  |Illum| | R |||
      ||      '/\\/ _(|===|-|   |  |''|  |:x:|=|  |inati| | Y |||
      ||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | Z |||
      ||       _(____)|===|+|[I]|DK|''|==|:x:|=|XX|<(*)>|=|^^^|||
      ||              `---^-^---^--^--'--^---^-^--^-----^-^---^||
      ||-------------------------------------------------------||
      ||_______________________________________________________||
      
      ''')
      
print("Welcome to the magic library!!!")

c1 = str(input("You see a bunch of books on the shelf.\nDK, I, Illuminati but one calls your attention more, as if you are being pulled by magic.\nDo you take it? "))

if c1 == "Yes" or c1 == "yes":
    print("You grabbed the book named, Black Magus.")
    c2 = str(input("Do you wanna read it? "))
    
    if c2 == "Yes" or c2 == "yes":
        print("You gained Fire Ball lv.1")
        
    elif c2 == "No" or c2 == "no":
         c3 = str(input("Do you save the book on your backpack? "))
         
         if c3 =="Yes" or c3 == "yes":
             print("You stored the book.")
    else:
         print("You put back the book.")
            
c4 = input("Do you grab any other book? ")

if c4 == "Yes" or c4 == "yes":
    book2 = str(input("Which book do you take DK, I, Illuminati or QRZY? "))

    if book2 == "DK":
        print("You suddenly feel cold and out of breath, you die.")
    
    elif book2 == "I":
        print("You lost your sense of self, and wandered off for eternity.")
    
    elif book2 == "illuminati":
        print("You feel fear from just grabbing it but also curiosity. You are compelled to leave it back in the shelf.")
    
    else:
        print("You died of boredom.")       
else:
   print("You died of boredom.")
    
              
            