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