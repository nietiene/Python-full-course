# exception chaining happens when exception is raised while handling another exception
# it help to track root cause of errors
# make debugging easier

# default chaining

try:
    int("abc")
except ValueError:
    raise TypeError("Converstion failed")


try:
    result = 1 / 0
except ZeroDivisionError as e:
    # as e stores the error object into variable e
    raise ValueError("some thing went wrong") from e
