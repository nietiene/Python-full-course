# exception chaining happens when exception is raised while handling another exception
# it help to track root cause of errors
# make debugging easier

# default chaining

try:
    int("abc")
except ValueError:
    raise TypeError("Converstion failed")
