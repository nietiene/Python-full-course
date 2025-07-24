# file handling lets your program read from or write to files on your computer
# common modes r, w, a, r+, b(binary mode)

# Reading a file
# make sure file exist
file = open("data.text", "r") 
content = file.read()
print(content)
file.close() # most important to free up memory