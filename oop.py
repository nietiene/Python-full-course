# class

# self is used to access vailables and method belong to the object but not global one 
class Car:
    def start(self):
      print("Car started")

# exceute an object fo car
my_car = Car()

# call only methoo
my_car.start()