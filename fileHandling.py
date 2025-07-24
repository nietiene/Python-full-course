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
# without with you may close file manually .close() 

# write using with 
with open("todo.txt", "w") as f:
    f.write("1. Study file handling\n")
    f.write("2. practice python")

# open file using with

with open("todo.txt", "r") as file:
    content = file.read()   
    print(content) 

# append file using with    
with open("todo.txt", "a") as file:
    file.write("\nThis is appended line")

# using try and catch
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

# working with JSON file in python
# 
import json # import json module

todo_list = [
    {"task":"learn file handling", "done": False},
    {"task":"learn file handling", "done": True}
]


with open("todo.json", "w") as file:
    json.dump(todo_list, file, indent=4)
# .dump() writes python data as .json file
# indent: makes it human-readable

# Load data from json
with open("todo.json", "r") as file:
    tasks = json.load(file)

# .load() used to loads or display files in json 
print(tasks)    

# update json file
# json.dumps -> convert python to json string
# .loads() -> convert json string to python

with open("todo.json", "r") as file:
    tasks = json.load(file)

tasks.append({"taks": "Build a project", "done": False})

with open("todo.json", "w") as file:
    json.dump(tasks, file, indent=4)