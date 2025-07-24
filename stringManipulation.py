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

# title
print("my nmae".title()) #out: My Name

# strip()
print(" hi ".split()) #out: hi

# lstrip()
print(" hi ".lstrip()) # "hi "

# replace
print("Hi there".replace("Hi", "Hello")) # Hello there