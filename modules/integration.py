import myOwnModules

# modules is function, variables or classes that you can import and use it in other file
print(myOwnModules.add(2,4))
print(myOwnModules.subtract(4,2))

# import specific function

from myOwnModules import add
print(add(4,200))

# Import and assign alias name

import myOwnModules as my

print(my.add(3,1))

# some builtin moodules

import math

print(math.sqrt(25)) # return 5

import random
print(random.randint(1, 100)) # ticks random number btn 1 - 100

import datetime
print(datetime.datetime.now()) # your current date and time