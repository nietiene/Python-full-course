# exception chaining happens when exception is raised while handling another exception
# it help to track root cause of errors
# make debugging easier

# default chaining

try:
    int("abc")
except ValueError:
    raise TypeError("Converstion failed")


try:
    result = 1 / 0 # this will generate error because dividing number by zero is not allowed in python
except ZeroDivisionError as e:
    # as e stores the error object into variable e
    raise ValueError("some thing went wrong") from e
    # frome e make new error linked to original one 
