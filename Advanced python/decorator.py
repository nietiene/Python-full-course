# decorator is function that takes another fuction as input and returns new function
# is used when you want to add functionality before ans after function runs
# used for logging, timing, authentication
# allows to add extra data without changing the function codes

# my_decorator takes func as input
def my_decorator(func):
    # wrapper function extends behavior of func()
    def wrapper():
        print("Before the function runs")
        func() # call original function
        print("After function runs")
    return wrapper

def say_hello():
    print("Hello")

decorator_function = my_decorator(say_hello)
decorator_function()     

# or use @ syntax

@my_decorator # this si the same as say_hello = my_decorator(say_hello)
def say_hello():
    print("hello")

say_hello()    


# functools.wraps

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result 