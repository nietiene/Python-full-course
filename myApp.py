print('Hello this is my first app')

# in python no semicolmn or baces are nedded

if 5 > 2:
    print("Five is greter than two")

# decrlation of variables

# datatype integer(int)
x = 5 # here is how we decrale variables in python
print(x) # print valiables

# string (str)
nane = "Etiene" 
print("My name is", nane)

# boolean (bool)
is_active = True
print(is_active)
# print() shows the output
# variables can be updated

nbr = 5
print("Value of number before update:",nbr)

nbr = nbr + 3
print("value of number after update",nbr)


# decralation of f-string usable dor readable output
# f before variables allows inserting variables directly inside braces
name2 = "Etiene"
age = 17
print(f"My name i {name2} and I am {age} years old."); 

# taking input to the user

# basic syntax: name = input(prompt) prompt is optional text displayed to the user

# name = input("Enter your name")
# print(f"hello {name}")

# since input() returns a string so to get number you must convert the input

# age = int(input("Enter your age:")) # convert the integer
# print(f"your age is {age}") 

# ///////list means collection of items//////////////
# items can be different datatype and we use squeare brackets []

fruits = ['Apple', 'Banana', 'Orange']
print(fruits)

fruits.append('Grape') # Add new item
print(fruits)

fruits[0] = "Mango" # Change fruit which belongs on index 0
print(fruits)

# ///////////dict (Dictionary)//////////////
# means unoedered collection of key-value pairs
# key must be unique and immutable(like strings or numbers)
# use curly braces {} with key: value

person = {
    "name": "Etiene",
    "age": 17,
    "city": "Kigali"
}
print(person)

# update value
person["city"] = "Bugesera"
print(person)

# Add new key-value
person["job"] = "Student"
print(person)

# ///////////////////tuple////////////////////
# immutable (can not changed after creation) collection of items
# use parantesis()
colors = ("red", "green", "blue")
print(colors)
print(colors[0])

# colors[0] = "cyan" # it will generate ERROR: turples does not support valiable assignment
# print(colors)

# /////////////////set///////////////////////
# unordered collection of unique items (no duplicates)
# mutable but element must be immutable
# use curly braces {} or set() constructor

numbers = {1, 2, 3, 2, 1}
print(numbers) # duplicates removed automatically

# Add new item
numbers.add(4)
print(numbers)

# Remove item
numbers.remove(2)
print(numbers)



# /////////////Arithimetic operators

# +, -, *, /, // floor division, %, ** exponentiation

# Example

a = 10
b = 3
print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.3333333333333333333
print(a // b) # 3 (flor divistion rounds down)
print(a % b) # 1 (remainder)
print(a ** b) # 1000

# ///////// Logical operators//////////////

x = 5
print(x > 3 and x < 0) # true if both conditions are true

print(x > 3 or x < 4) # true if first condition is true

print(not(x > 0)) # true if is false

# ///////// comparison operator
x = 50
y = 50
print(x == y) # true
print(x != y) # false
print(x < y)  # false
print(x > y)  # false
print(x <= y) # true
print(x >= y) # true


# ////// conditional statements
# it lets your program make decisions

#  if statement
age = 50
if age >= 18:
    print("you are an adult.")

# if.... else statement
if age >= 18:
   print("you are adult")
else:
    print("You are not adult")   