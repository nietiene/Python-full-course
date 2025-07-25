# map is used to appy fucntion to every item in list
# syntax map(function, iterable)

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)