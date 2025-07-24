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
    x = 10/ 2 # if this code runned without error the python skips the 
except:
    print("Error happened.")
finally:
    print("This will always run")    
