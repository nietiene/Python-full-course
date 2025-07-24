# file handling lets your program read from or write to files on your computer
# common modes r, w, a, r+, b(binary mode)

# Reading a file
# make sure file exist
# .read() reads a whole file as one string
# .readLine() reads one line at one time
#  .readlines() return a list of lines

file = open("data.text", "r") 
content = file.read()
print(content)
file.close() # most important to free up memory

file = open("data.text", "r")
for line in file:
    print(line.strip())
file.close()    
