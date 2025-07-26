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
# print(next(it)) # print ERROR: stopIteration

# print a text line by line

file = open("notes.txt", "r")
it = iter(file)
print(next(it)) # first line
print(next(it)) # second line


# create your own iterator which will count from 1 to 5

class CountToFive:
    def __init__(self):
        self.num = 1 # start from one

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            result = self.num
            self.num += 1
            return result
        else:
            raise StopIteration
