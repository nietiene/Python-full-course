# creating string
s = "Hello"

# Accessing characters and slices 

a = "Python" # Accessing character using index
print(a[0])
print(a[-1]) # Accessing last character

# Slicing[start:end:step]
s = "Python"
print(s[0:3]) # start from index 0 up to  index 3
print(s[2:]) # start from index 2 to the end
print(s[:4]) # from start or index 0 to index 4
print(s[::2]) # output: Pto (every 2nd char)
# start from index 0 and s return every second character
print(s[::-1]) # Reverse string

# common string method
# lower which return the string into lower case letter
print("Hello".lower())

# upper
print("Hello".upper()) #Out: HELLO

# capitalize
print("hello".capitalize()) # out: Hello

# title capitalize first character to each word
print("my nmae".title()) #out: My Name

# strip() removes leading(right) and trailling(left) white whitespace
print(" hi ".split()) #out: hi

# lstrip() removes only leading(left) space
print(" hi ".lstrip()) # "hi "

# rstrip() removes only trailing(right) spaces
print(" hi ".rstrip())

# replace(old, new)
print("Hi there".replace("Hi", "Hello")) # Hello there

# split() split a sring using into parts using separator(,)
print("a, b, c".split(",")) #output: ['a','b','c']

# join joins a list of string into one string using separator
print(",".join(['a', 'b', 'c'])) # a, b, c

# find(sub) find index of number
print("Hello".find("l")) # out: 2

# count(sub)
print("Hello".count("l"))

# endswith()
print("Hello".endswith("lo")) #out: True

# isdigit()
print("123".isdigit()) # out: True

# isalnum()
print("abc123".isalnum()) # out: True