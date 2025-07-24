# class

# self is used to access vailables and method belong to the object but not global one 
# when you call method without self it will generate an error
class Car:
    def start(self):
      print("Car started")

# exceute an object fo car
my_car = Car() # create an object

# call only methood
my_car.start() # call the method