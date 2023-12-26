import math
def add (x,y):
    return x + y

def sub (x,y):
    return x - y

def module (x,y):
    return x % y

def division (x,y):
    return x / y

def multiplication (x,y):
    return x * y

def power (x,y):
    return pow (x,y)

def sin (x,y):
    return math.sin(x), math.sin(y)

def cos (x,y):
    return math.cos(x), math.cos(y)

def tan (x,y):
    return math.tan(x), math.tan(y)

def sqrt (x,y):
    return math.sqrt(x), math.sqrt(y)

def log (x,y):
    return log(x), log(y)

print("Select your operation.")
print("1) Addition.")
print("2) Substraction.")
print("3) Division.")
print("4) Multiplication.")
print("5) Power.")
print("6) Square Root.")
print("7) Sin.")
print("8) Cos.")
print("9) Tan.")
print("10) Log.")
print("11) Module.")


operation = input('Enter your operation from 1 to 11: ')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if operation == "1":
    print (num1 , ' + ' + num2 , " = " , add(num1,num2))
    
elif operation == "2":
    print (num1 , ' - ' , num2 , ' = ' , sub(num1,num2))
    
elif operation == "3":
    print (num1 , ' / ' , num2 , ' = ' , division(num1,num2))
    
elif operation == "4":
    print (num1 , ' * ' , num2 , ' = ' , multiplication(num1,num2))
    
elif operation == "5":
    print (num1 , ' ^ ' , num2 , ' = ' , power(num1,num2))
    
elif operation == "6":
    print ('sqrt(num1), sqrt(num2)' , ' = '  , sqrt(num1,num2))
    
elif operation == "7":
    print ('sin(num1), sin(num2)' , ' = ' , sin(num1,num2))
    
elif operation == "8":
    print ('cos(num1), cos(num2)' , ' = ' , cos(num1,num2))   
    
elif operation == "9":
    print ('tan(num1), tan(num2)' , ' = ' , tan(num1,num2)) 
    
elif operation == "10":
    print ('log(num1), log(num2)' , ' = ' , log(num1,num2))

elif operation == "10":
    print (num1 , ' % ' , num2 , ' = ' , module(num1,num2))
    
else :
    print ('Invalid number')    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    