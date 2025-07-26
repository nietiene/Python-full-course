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
    def __init__(self): # runs automatically when you create new object
        self.num = 1 # start from one(initialization of attribute which will start from one)

    def __iter__(self): # this __iter__ make object as iterable
        return self

    def __next__(self): # special methood called every time you want to move to next item
        if self.num <= 5: # checks if current number is lees that or equal to 5
            result = self.num # save current number into variable
            self.num += 1 # it increates at one so when you ask to move to next number it moves forward
            return result
        else: # if number is greater than 5
            raise StopIteration
        # raise is uded to throw an exception which tells python something went wrong
        # it stops the execution
        

counter = CountToFive()
# access attribute
# print(counter.num)


# for number in counter:
#     print(number)

# or use manual method
it = iter(counter)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) # ERROR

# generator is simple way of create iterator using yield instead of return to produce sequence of values at one time

def my_gen(): # here is generator function
    yield 1 # yield is used to safe state 
    # yield is like return but it pauses the function and saves its state
    # return only it ends thre function, returns the value, cant resume the function
    # next time you call generator it resumes where you lef off
    yield 2
    yield 3

gen = my_gen() # create a generator object

print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3


def count_upt_to(max):
    n = 1
    while n <= max:
        yield n
        n += 1

for num in count_upt_to(3):
    print(num)        