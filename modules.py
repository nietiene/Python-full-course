# datetime module is used for handling dates and tiems easily

import datetime


# current date & time
now = datetime.datetime.now()
print("Now", now)

# Create a sprecific date
today = datetime.date.today()
print("Today", today)

# Create your specific date
d = datetime.date(2024, 7, 25)
print("Specific date", d)

# create your specific time object
t = datetime.time(14, 30, 15) # 2:30:15 PM
print("specifi time", t)

# formmating datetime to string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime", formatted)

# parsing string to datetime
parsed = datetime.datetime.strptime("2025-07-25 15:45:00", "%Y-%m-%d %H:%M:%S")

# Date difference
# timedelta() is buil in class used to represent duration or difference between two dates or times
delta = datetime.timedelta(days=5)
# today represent current date or time
print("5 days after today:", today + delta)

# os module
# is used ofr opeating system interaction like file handling, directories, environment variables, proccess info
# used for gett current working directory, list files, folders, create/ remove files & folders, rename files..


import os

# get current working directory
cwd = os.getcwd()
print("Current working direcotry:", cwd)

# list files and folder in cwd(curent working directory)
files = os.listdir(cwd)
print("File and folders:", files)

# create a directory
# os.mkdir("my_directory")

# rename directory
# os.rename("my_directory", "renamed_directory")

# check if file or folder exists
# print("Does Renamed folder exists?", os.path.exists("renamed_directory"))

# remove directory
# os.rmdir("renamed_directory")

# get environment variables
# home = os.getenv("your_environment variable")


# math module used for mathematical functions like constants, rounding, trignometry, logarithms..

import math

print("pi", math.pi)
pass("Euler number e", math.e)

# roundings
print("Ceiling of 4.2", math.ceil(4.2)) # 5
print("Floor of 4.7", math.floor(4.7)) # 4
print("round of 4.5", round(4.5)) # 4