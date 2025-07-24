import myOwnModules

print(myOwnModules.add(2,4))
print(myOwnModules.subtract(4,2))

# import specific function

from myOwnModules import add
print(myOwnModules.add(4,200))

# Import and assign alias name

import myOwnModules as my

print(my.add(3,1))