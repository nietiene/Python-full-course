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


# timing measure how long function takes to run

import time # is used to measure time before ans after function runs
import functools # provides tool used to preserve the original function name ..


def timer(func):
    @functools.wraps(func) # keeps the orignal function name
    def wrapper(*args, **kwargs): # accept any arguments numbers or list
        start = time.time() # starts the stop watch
        result = func(*args, **kwargs) # call the actual function
        end = time.time() # stop the stopwatch
        # funct.__name__ this calls the orignal function name
        # calculate the seconds by subtracting end and start
        # :.4f this shows number as float shows four digit after the decimal point
        print(f"{func.__name__} took {end - start:.4f} seconds") # report time
        return result # return orignal result
    return wrapper

@timer
def waste_time(num):
    for _ in range(num):
        sum([i**2 for i in range(10000)])

waste_time(10)        