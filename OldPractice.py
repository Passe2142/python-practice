# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:33:30 2020

@author: Jules
"""



# Ask the user to input their name and assing it to a variable name "name"
#
name = input('Choose your username: ')

print ('Thanks for being at the numbers operation facility', name,'!')

#Ask the user to input 2 values and store them in variables in num1 and num2
#Convert the string into regular number
#Add the values entered and store the sum
#Subtrac values and store in a variable name diference
#Multiply the values and store in a product
#Divide the values and store in quotient
#Use modulus on the values to find the remainder
#Print the results
num1, num2 = input('Input two values: ').split()

num1 = float(num1)
num2 = float(num2)

sum = num1 + num2
diference = num1 - num2
multiply = num1 * num2
quotient = num1 / num2
modulus = num1 % num2

print('The sum of the values is equal to: {} + {} = {}'.format(num1, num2, sum))
print('The diference of the values is equal to: {} - {} = {}'.format(num1, num2, diference))
print('The multiplication of the values is equal to: {} * {} = {}'.format(num1, num2, multiply))
print('The quotient of the values is equal to: {} / {} = {}'.format(num1, num2, quotient))
print('And the modulus of the values is equal to: {} % {} = {}'.format(num1, num2, modulus))


# Problem allow the user to enter miles and convert to km
# km = miles * 1.60934
# enter 5 miles
# 5 miles equals to 8.04 km

miles = input('Miles convertion to kilometers: ')

miles = float(miles)

km = miles * 1.60934

print (miles,'miles are',km,'kilometers')  

# Calculator
# enter calculation 5 * 6 

# 5 * 6 = 30
# store the user input of numbers of 2 and the operator
# convert the string into ingers/float
# if  +  provide output based on addition

# print resutl



message1 = '{0} is easier than {1}'.format('Python', 'Java') 
message2 = '{1} is easier than {0}'.format('Python', 'Java') 
message3 = '{:10.2f} and {:d}'.format(1.234234234, 12)
message4 = '{}'.format(1.234234234)


Edad_de_Usuario1 = [6,8,12,7,25,15]
Edad_de_Usuario1[2:4]


myList = [1, 2, 3, 4,5, 'Hello']

print (myList)





# We'll provide different output based on age 
# 1 - 18 -> Important
# 21 , 50 >65 -> Important
# All others -> Not Important

# Recive age and store in age

age = eval(input('Enter age: '))

# and: if both conditions are true it returns true
# or : if either condition is true then true 
# not : Convert a true condition into a false on



# if age is both greater than or equal to 1 and less than or equal to 18 
 
if (age >= 1) and (age <= 18):
    print ("Important Birthday, congratulations you wont die becouse of corona virus!")


# if age is either 21 or 50 Important

elif (age == 21) or (age == 50):
    print ("You suck you are not important , just kidding!")

elif not (age < 65):
    print('Belongs in the risk group!')
 

else:
    print('Not important')
# We check if age is less than 65 and then convert true to false 


# else not important for Ju

# Problem , input age

age = input('Introduce your age: ')

age = int(age)
# if the age 5 to kindergarten

if (age <= 5):
    print('Go to kindergarden')


# ages throu 6 to 17 goes to grades 1 to 17

elif (age >= 6) and (age <= 17):
    print("Goes to middle school or highschool")

# if age is greater then 17 say go to college

else:
    print('Go to college')

# try to complete this program with 10 or less lines


#





















