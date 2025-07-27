# Regex is way of  of search, match, and manipulate strings using patterns

""""
   ////Basic Regex functions/////
   re.search() -> search for anywhere in string 
   re.match() -> matches from beginning of string
   re.findall()  -> return all matches as list
   re.sub() -> replace pattern with something else
"""

import re

text = "My email is example@gmail.com"

# \w+ one or more word characters(letters, digits, underscre)
# @ the symbol must be included
# \w+ one or more word characters again
# '. a literal dot
# \w+ one or more characters

# re.search() it searches for the first occurence of given pattern anywhere inside the string
# 
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print("Found", match.group())
    # match.group() -> returns the exact substring that matched the pattern


# using re.findall()

text = "My numbers are 123, 456, and 789"
# \d matches any digit
# +
numbers = re.findall(r'\d+', text)
print(numbers)
