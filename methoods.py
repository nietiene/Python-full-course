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
upper_Words = list(map(str.upper, words))
print(upper_Words)

# filter() is used to filter out items from list based on condition
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# filter words longer that 4 characters
# w stands for each item in words list
words = ['cat', 'elephant', 'dog', 'tiger']
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)