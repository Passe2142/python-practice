# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:00:03 2020

@author: Jules
"""

# Sheet paper with basic coding for python.

# Variables ->  Are names given to data.They store data be it strings or numbers.

# Basic areithmetic operators : + , - , * , / , % (modulus) , ** (to the power).

# Strings refer to text and go in quotes "Example".

# Numbers can be integers (Z) or floats they have decimal parts like this 1.365.

# Format , can work with % operator : %s (for strings), %d (for integers), %f (for floats).

# Example

brand = "Apple" # brand is the variable that stores the string Apple

exchangeRate = 1.235235245

message = "The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR"%(brand, 1299, exchangeRate)

print (message)

# result : The price of this Apple laptop is 1299 USD and the exchange rate is 1.24 USD to EUR

# Format with curly brackets too {}

# The parameter ‘Apple’ has a position of 0, 1299 has a position of 1 and 1.235235245 has a position of 2.

message1 = "The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR".format("Apple", 1299, 1.1235235245)

print (message1)

# The price of this Apple laptop is 1299 USD and the exchange rate is 1.12 USD to 1 EUR

# Note: If you do not want to format the string, you can simply write :
        
# message1 = ‘The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR’.format(‘Apple’, 1299, 1.235235245)

# The interpreter will replace the curly brackets based on the order of the parameters provided.

# Equal sign "=" has a diferent meaning in coding, it assigns data to a variable: y = 5 means y <- 5, 5 is "store in y".
                  
# Casting is converting from one form of data to another type of data , such as from an integer to a string.

# Built in functions on python: int(), str(), float() these cast data and we cannot type int("Hello") or int("4.22321").

# Lists refer to a collection of data which are normaly related.

# UserAge = [7,88,45,24,15] the list values are accesible by their indexes , they start from 0

# UserAge[0] = 7 and so on

# I can assing list to variables or a part of it

# Examples: userAge2 = userAge , the variable userAge2 becomes [7,88,45,24,15].

# If you write userAge3 = userAge[2:4], you are assigning items with index 2 to index 4-1.

# You can modify and append the lists.

# Tuples : are like list but you cannot modify their values , they will stay the same for the rest of the progam.

# To writ Tuples use the brackets (), for example :
    
#                       monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# Conclusion : A list is an ordered collection of things. You don't know ahead of time how long it is, or what in particularly is in any spot.

# This is why lists tend to be groups of similar objects - you're going to do some common operation to all of them.

# A tuple, on the other hand, is set in size, which means you know exactly what is in each index. 

# Dictionary : is a collection of related data pairs, we use {} to declare dictionaries. For example name and age 

# dictionaryName = {dictionary key : data}

# The "dictionary key" must be unique 

# Expmple : Name_and_Age = {"Jules":24, "Carlos":60, "Alicia":57, "Ariel":21}

# Also you can declare a dictionary using the dict()

# Name_and_Age = dict(Jules = 24, Carlos = 60, Alicia = 57, Ariel = 21)

# To make the program interactive we can use these built in functions : input() to make the user enter data and print() to call out data

# Escape characters: are use to print special "unprintable" characters.

# We use \t to create a tabulation ,\n to create a new line , \\ to print \ , \" prints a double quote and \' prints a single quote.

# Condition Statements :

# All control flow tools involve evaluating a condition statement. The program will proceed differently depending on whether the condition is met.

# # Logical Conditions: And , or , not : 
    
#                                   Not equal : !=
#                                   Greater than :  2>1                             
#                                   Smaller than :  2<3
#                                   Greater or equal than : 3>=2
#                                   Smaller or equal than : 4<=5
#                                   Equal : ==                 

#

# If statement : one of the most commonly used flow control statements 

# if condition 1 is met:
#     do A
# elif condition 2 is met:
#     do B 
# elif condition 3 is met:
#     do C 
# elif condition 4 is met:
#     do A
# else:
#     do E

# You can have as many "elif" you like.

# Example :

userInput = input('Enter 1 or 2: ')
if userInput == "1": 
    print ("Hello World")
    print ("How are you?") 
elif userInput == "2":
    print ("Python Rocks!")
    print ("I love Python")
else:
    print ("You did not enter a valid number")

# Inline If : an inline statement is a simpler form of an if statement and is only more convinent to perform a simple task

# Do Task A if condition is true else do Task B

# Loop : This execute a block of code repeatedly until the condition for the statement is no longer valid.

# Looping through an iterable 

# In Python, an iterable refers to anything that can be looped over, such as a string, list or tuple. 

# The syntax for looping through an iterable is as follows:

# for a in iterable:
    
# print (a)

# Example : 

    
pets = ['cats', 'dogs', 'rabbits', 'hamsters']

for myPets in pets:
    print (myPets)

#

# In the program above, we first declare the list pets and give it the members 'cats' , 'dogs' , 'rabbits' and 'hamsters'.

# Next the statement "for myPets in pets": loops through the pets list and assigns each member in the list to the variable myPets.

# The first time the program runs through the for loop, it assigns ‘cats’ to the variable myPets . 

# The statement print (myPets) then prints the value ‘cats’ . 

# The second time the programs loops through the for statement, it assigns the value ‘dogs’ to myPets and prints the value ‘dogs’ .

# The program continues looping through the list until the end of the list is reached.

# We can also display the index of the members in the list. We use the enumerate() function.

for index, myPets in enumerate(pets):
    print (index, myPets)

# The next example shows how to loop through a string.   

message = "Hello"

for i in message:
    print(i)


# Looping through a condition of numbers :

# To loop through a sequence of numbers, the built-in range() function comes in handy.

# The range() function generates a list of numbers and has the syntax range (start, end, step) .

# If start is not given, the numbers generated will start from zero.

# Note: A useful tip to remember here is that in Python (and most programming languages), unless otherwise stated, we always start from zero. 

# For instance, the index of a list and a tuple starts from zero.

# When using the format() method for strings, the positions of parameters start from zero. 

# When using the range() function, if start is not given, the numbers generated start from zero.

# Example :
    
# range(5) will generate the list [0, 1, 2, 3, 4] 

# range(3, 10) will generate [3, 4, 5, 6, 7, 8, 9] 

# range(4, 10, 2) will generate [4, 6, 8]

for i in range(5):
    print (i)   


# While loop : a while loop repeatedly executes instructions inside the loop while a certain condition remains valid.

# while condition is true:
#     do A

# Most of the time when using a while loop, we need to first declare a variable to function as a loop counter.

# Let’s just call this variable counter .

# The condition in the while statement will evaluate the value of counter to determine if it smaller (or greater) than a certain value. 

# If it is, the loop will be executed.

counter = 5

while counter > 0:
    print ("Counter = ", counter) 
    counter = counter - 1

# Break : When working with loops, sometimes you may want to exit the entire loop when a certain condition is met.

# 

j = 0

for i in range(5): 
    j = j + 2 
    print ("i = ", i, ", j = ", j) 
    if j == 6: 
        break

# Without the break keyword, the program should loop from i = 0 to i = 4 because we used the function range(5) .

# However with the break keyword, the program ends prematurely at i = 2. 

# This is because when i = 2, j reaches the value of 6 and the break keyword causes the loop to end.

# In the example above, notice that we used an if statement within a for loop. It is very common for us to ‘mix-and-match’ various control tools.

# In programming, such as using a while loop inside an if statement or using a for loop inside a while loop.

# This is known as a nested control statement.

# Continue : When we use continue , the rest of the loop after the keyword is skipped for that iteration .

j = 0 
for i in range(5):
    j = j + 2
    print ("\ni = ", i, ", j = ", j)
    if j == 6:
        continue
    print ("I will be skipped over if j=6")


# Try, Except is the final control statement. This statement controls how the program proceeds when an error occurs.

# try: 
#   do something
#    except:
#        do something else when an error occurs 

# Example 1 :

try: 
    answer = 12/0 
    print (answer) 
except:
    print ("An error occurred")

# Example 2 :
    
try:
    userInput1 = int(input("Please enter a number: ")) 
    userInput2 = int(input("Please enter another number: ")) 
    answer = userInput1/userInput2 
    print ("The answer is ", answer) 
    myFile = open("missing.txt", 'r')
except ValueError:
    print ("Error: You did not enter a number") 
except ZeroDivisionError:
    print ("Error: Cannot divide by zero") 
except Exception as e:
    print ("Unknown error: ", e)


# The list below shows the various outputs for different user inputs. >>> denotes the user input and => denotes the output. 

#  >>> Please enter a number: m 

#  => Error: You did not enter a number 

#  Reason: User entered a string which cannot be cast into an integer. This is a ValueError.

#  Hence, the statement in the except ValueError block is displayed. 

#  >>> Please enter a number: 12

#  >>> Please enter another number: 0

#  => Error: Cannot divide by zero  

#  Reason: userInput2 = 0. Since we cannot divide a number by zero, this is a ZeroDivisionError.

#  >>> Please enter a number: 12 

#   >>> Please enter another number: 3 

#   => The answer is 4.0 

#   => Unknown error: [Errno 2] No such file or directory: 'missing.txt'   

#   Reason: User enters acceptable values and the line print ("The answer is ", answer) executes correctly. 

# However, the next line raises an error as missing.txt is not found. 

# Since this is not a ValueError or a ZeroDivisionError , the last except block is executed. 

# ValueError and ZeroDivisionError are two of the many pre-defined error types in Python. 

# ValueError is raised when a built-in operation or function receives a parameter that has the right type but an inappropriate value.

#  ZeroDivisionError is raised when the program tries to divide by zero. 

# Other common errors in Python include  :

# IOError: Raised when an I/O operation (these are input/output operation such as the built-in open() function) fails for an I/O-related reason “file not found”. 

# ImportError: Raised when an import statement fails to find the module definition.

# IndexError: Raised when a sequence (e.g. string, list, tuple) index is out of range.  

# KeyError: Raised when a dictionary key is not found.  

# NameError: Raised when a local or global name is not found.  

# TypeError: Raised when an operation or function is applied to an object of inappropriate type.

#

#

#

#






















