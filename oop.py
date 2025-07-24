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


# Encapsulation

class BankAccount:
   def __init__(self, balance):
      self.balance = balance # private

   def deposit (self, amount):
        self.__balance += amount

   def show_balance(self):
      print(f"Balance: ${self.__balance}")     

acc = BankAccount(1000)
acc.deposit(500)
acc.show_balance()      
