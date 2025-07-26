# iterator lets you loop through elements one at one using next
# lets you loop only one item at one time
my_list = [10, 20, 30]
# iter() turns the list into iterator object means make it being looped as one time
it = iter(my_list)

print(next(it)) # gets the first value
print(next(it)) # next one
print(next(it)) # also next one

text = "DOG"
it = iter(text)
print(next(it)) # print D
print(next(it)) # print O
print(next(it)) # print G
print(next(it)) # print ERROR: stopIteration