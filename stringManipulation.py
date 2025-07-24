# creating string
s = "Hello"

# Accessing characters and slices 

a = "Python" # Accessing character using index
print(a[0])
print(a[-1]) # Accessing last character

# Slicing[start:end:step]
s = "Python"
print(s[0:3]) # start from index 0 up to  index 3
print(s[2:]) # start from index 2 to the end
print(s[:4]) # from start or index 0 to index 4
print(s[::2]) # output: Pto (every 2nd char)
# start from index 0 and s return every second character
print(s[::-1]) # Reverse string

# common string method
# lower which return the string into lower case letter
print("Hello".lower())

# upper
print("Hello".upper()) #Out: HELLO

# capitalize
print("hello".capitalize()) # out: Hello

# title capitalize first character to each word
print("my nmae".title()) #out: My Name

# strip() removes leading(right) and trailling(left) white whitespace
print(" hi ".split()) #out: hi

# lstrip() removes only leading(left) space
print(" hi ".lstrip()) # "hi "

# rstrip() removes only trailing(right) spaces
print(" hi ".rstrip())

# replace(old, new)
print("Hi there".replace("Hi", "Hello")) # Hello there

# split() split a sring using into parts using separator(,)
print("a, b, c".split(",")) #output: ['a','b','c']

# join joins a list of string into one string using separator
print(",".join(['a', 'b', 'c'])) # a, b, c

# find(sub) find index of number
print("Hello".find("l")) # out: 2

# count(sub) counts how many times a string appears 
print("Hello".count("l"))

# startswith() check if string startswith the given prefix
print("Hello".startswith("He")) # out: True

# endswith()
print("Hello".endswith("lo")) #out: True

# isdigit() return true if all characters are digits
print("123".isdigit()) # out: True

# isalnum() returns true if all characters are letters or digit(no spaces, symbol)
print("abc123".isalnum()) # out: True

# Escape character and Raw Strings
# \t, \', ", \\

print("Hello\nWorld") # returns  each world to newline

# List Comprehension is way of create lists or dictionary using single of code

squeare = [x ** 2 for x in range(5)]
# 0 ** 2 = 0
# 1 ** 2 = 1
# 2 ** 2 = 4
# 3 ** 2 = 9...
print(squeare)

# filtering even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# convert strings to lowercase
names = ["ETIENE", "NIYOMUGABO", "PYTHON"]
lowered = [name.lower() for name in names]
print(lowered)

# Add if/else inside 
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(labels)

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)

# Dictionary comprehenson
squares = {x: x ** 2 for x in range(2)}
print(squares)

# Basic calculator

number1 = float(input("Enter first number number: "))
operator = input("Enter symbols")
number2 = float(input("Enter second number: "))

# basic culculator
def calculator():
  if operator == "+":
      print(number1 + number2)
  elif operator == "-":
      print(number1 - number2)
  elif operator == "*":
      print(number1 * number2)    
  elif operator == "/":
     if number2 == 0:
        print("Error: Dvision by zero is not allowed.")
     else:   
        print(number1 / number2)
  else:
     print("Enter a valid")

calculator()        

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# keep ask until user guesses correctly
while True:
   gues = int(input("Guesse the number (1-100)"))

   if gues < secret_number:
      print("Too low! try again.")
   elif gues > secret_number:
      print("Too high! try again.")
   else:
      print("🎉 congratulations! you guessed it right")      
        
