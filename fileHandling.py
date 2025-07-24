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
    print(line.strip()) # .strpi() removes \n
file.close()    


# Writting to a file
# w is write mode if file exist the content erased else it created
file = open("notes.txt", "w")
file.write("Hello, file!\n")
file.write("This is second line.")
file.close()

# Appending to a file
file = open("notes.txt", "a")
file.write("\nthis is line added to the end")
file.close()

# using with statement
# with handles closing file automatically even an error happens preferred for clean and safe code

# write with 

with open("todo.txt", "w") as f:
    f.write("1. Study file handling\n")
    f.write("2. practice python")