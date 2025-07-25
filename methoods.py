# map is used to appy fucntion to every item in list
# syntax map(function, iterable)

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# without lambda
# because map does not return list directly we need to use list()
def square(x):
    return x ** 2
print(list(map(square, nums))) # here it will square each number in num list


# converting string to upper case
words = ['hello', 'python', 'world']
# str is built-in string class in python used to access string methood like upper(), lower(), strip()
upper_Words = list(map(str.upper, words))
print(upper_Words)

# filter() is used to filter out items from list based on condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# filter words longer that 4 characters
# w stands for each item in words list
words = ['cat', 'elephant', 'dog', 'tiger']
# len() is built-in function used to return length of items it count a number of character in the string
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)


# reduce() is used to combine all items to one

from functools import reduce
# syntax: reduce(fuction, iterable)

nums = [1, 2, 3, 4, 5]
# x is previous result and y is next number from the list
product = reduce(lambda x, y: x * y, nums)
print(product)