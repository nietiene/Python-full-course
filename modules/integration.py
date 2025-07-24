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