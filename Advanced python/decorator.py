# decorator is function that takes another fuction as input and returns new function
# is used when you want to add functionality before ans after function runs
# used for logging, timing, authentication

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After function runs")
    return wrapper

def say_hello():
    print("Hello")

decorator_function = my_decorator(say_hello)
decorator_function()     

# or use @ syntax

@my_decorator
def say_hello():
    print("hello")
say_hello()    