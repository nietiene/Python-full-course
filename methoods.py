# map is used to appy fucntion to every item in list
# syntax map(function, iterable)

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# without lambda
def square(x):
    return x ** 2
print(list(map(square, nums)))