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