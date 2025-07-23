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

#  if.....elif....else
score = 75
if score >=90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
   print("Grade C") # this is result
else:
    print("Grade F")     

# python checks condition in order 
# if first condition is true get executed and then the rest are skipped

# Nested is statement
# Pyton use indentations space between words
age = 20
had_id = True

if age >= 18:
    if had_id:
       print("You are adult")
    else:
      print ("You need an ID.")   
else:
    print("You are too young")      

# short if (one-liner)
if x > 0: print("Positive number") 

# Ternary operator (short if/ else)
age = 17
message = "Adult" if age > 18 else "Minor"
print(message)

# logical opeator with conditions
# 
age = 25  
has_ticket = True

if age >= 18 and has_ticket:
    print("Allowed in")

# loops
# for loop used when you know how many times to loop

fruits = ['Apple', 'Banana', 'cherry']
# for each item in the list of fruits do something
for fruit in fruits:
    print(fruit) # print each item in the list; output is Apple, Banana, cherry

# Looping over number
# Range start from zero and before a number you mentioned
for i in range(5):
    print(i) # output: 0, 1, 2, 3, 4

# range(start, stop, step)
#  start: where to begin
# stop: where to stop but it does not included
# step: how much to increase
for i in range(2, 10, 2):
    print(i)   # output: 2, 4, 6, 8 

# Looping through a dictionary
person = { "name": "john", "age": 25 }
for key in person:
    print(key) # outpu: name, age

# Looping through key-value pairs

for key, value in person.items():
    # .items() gives you a list of key-value like this [("name", "etiene"), ("age": 22)]
    print(key, value)

# using for to get index
colors = ['Red', 'Blue', 'Green']
# enumerate() function adds a counter (index number) to each item in the list
for index, color in enumerate(colors):
    print(index, color) 
    print(list(enumerate(colors)))    

# looping with break and continue
# break stops look early

for b in range(20):
    if b == 5:
       break
    print(b) # output: it will loop but then stops on four

# Continue: skip the step and continue to next item
for b in range(5):
  if b == 2:
      continue
  print(b) 

#  nested for loops

for c in range(3): # here the c is three numbers 0, 1, 2
    for j in range(2): # here for each time c changes loop the two number 0, 1 so looping two times very c changes
        print("c",c, "j",j) 

# while loop (repeat while condition is true)

count = 0

while count < 3:
    print("Counter", count)
    count += 1  

# infinite loop

# while True:
#     print("I will run forever") 

# Multiplication table
for i in range(1, 6):
    for j in range(1, 6): # at each time a i will change we will print it for five times
       print(i * j, end='\t') # end='\t' means dont go to next line just put a tab space like a table column
    print()   # print a new line after finishing one row
    
    #   1 * 1 = 1
    #   1 * 2 = 2
    #   1 * 3 = 3
    #   1 * 4 = 4
    #   1 * 5 = 5
    # and it printend as 1 2 3 4 5