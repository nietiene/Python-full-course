# error handling means deal with unexpected problems
try:
    num = int("Hello")
except:
    print("You must enter a number")    

try:
    x = 5 / 0
except ZeroDivisionError:
   print("You ca't divide by zero.")
except ValueError:
   print("Wrong value")

try:
    print("Every thing is fine.")
except:
    print("An erro happened.")
else:
    print("No error occured")   

# output: everything is finr. no error occured    

# using finally always run 
try:
    x = 10/ 2 # if this code runned without error the python skips the except block
except:
    print("Error happened.")
finally:
    print("This will always run")    

# while True:
#     try:
#         age = int(input("Enter age:"))
#         print("Your age is:", age)
#         break
#     except ValueError:
#         print("Please enter a valid number")

# creating your own error or bug
# use raise keyword
# def set_age(age):
#     if (age < 0):
#         raise ValueError("Age cannot be negative")
#     print("Age is:", age)

# set_age(-5)    

# input and output in python
# input taking input from the user using input()
# printing or displaying out to the user using print()

# Method of formatting a string
name = "Etiene"
age = 20
print(f"My name is {name} and I'm {age} years old")

# method two using format()
print("my name is {} and I am {} years old".format(name, age))

# using % methood

# %d stands for decimal or integer
# %s stands for string
print("My name is %s and I am %d years old" % (name, age))

# reading two numbers in one line
a, b = input("Enter a two numbers").split()
print("You entered:", a, "and", b)