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

match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print("Found", match.group())