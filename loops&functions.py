# nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1 

# for eahc time  i will runs also j will runs twice
# i=1, j=1
# i=1, j=2    

#  else with while loop
x = 1
while x > 4:
    print(x)
    x += 1
else:
    print("Loop finished")    

# when you use break will not run
# x = 1 
# while x > 5:
#     print(x)
#     if x == 2:
#     break # automaticaly here it generate an error
#    x + 1
# else:
# print("This wont run")

# Menu system usin while loop

# while True: # it will keep showing menu until you break
#     print("\nMenu:") # \n calls newline character it starts new line when printing
#     print("1. say hello")
#     print("2. Exit")
#     choice = input("Choose option")

#     if choice == "1": # here it will checks if user type 1
#        print("Hello word")
#     elif choice == "2": # here also check if user 
#         print("Good bye!")
#         break
#     else:
#         print("Invalid choice. Try again")

def say_hello(): # we use def to define function
    print("Hello guyz!")

say_hello() # function call

#  greetings of parameter
def greet(name):
    print("Hello", name)
greet("Etiene")    
greet("Alice")    

#   Adding numbers
def add(a, b):
    print(a + b)
add(1, 3)   

# Returning values with return
def square(x):
    return x * x # you can store the return value or use it directly
# print(square(4))
result = square(4)
print(result)

# Default parameters
def greet(name = "Guest"):
    print("Hello", name)
greet() # hello Guest
greet("Etiene") # hello name    

# keyWord arguments
# ou can call function using keyword=value
def student_info(name, age):
    print(f"Nmae: {name} age {age}")
student_info(name="etiene", age=30)    

# Variable length arguments
# *args when you dont know how many arguments will be passed
# **kwargs when you want to accept named arguments like key-value
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total
    
print(add_all(1, 2, 3, 4))    

# **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
print_info(name="Etiene", age=17, school="Gikonko")        
    

# local scope and grobal scope

# local scope
def show():
    x1 = 40
    print(x1) 
show() # outp:20
# print(x)  ERROR:

# Grobal scope

x = 30
def showA():
    print(x)
showA()
print(x)    

# if you want to midifiy grobal inside the function use grobal keyowrd

x = 2

def modif():
    global x
    x = 10

modif()

# Lambda funcition (Anonymous function)
# use only one-line means short function
# lambda is used to create small, anonymous function (function without name)
square = lambda x: x * x
print(square(6))