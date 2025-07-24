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

# (__) make your attribute private 
class BankAccount:
# __init__ this is destructor runs automatically when you create a new object  
# self is current object for being created
# balance is value passed when you're creating an object 
   def __init__(self, balance):
    # self.__balance it creates private variable(which can not easily accessed outside) which will store accounts balance
      self.__balance = balance # private

   def deposit (self, amount):
        self.__balance += amount

   def withDraw (self, amount):
      if self.__balance >= amount:
         self.__balance -= amount
      else:
         print("not enought balance")        

   def show_balance(self):
      print(f"Balance: ${self.__balance}")     

acc = BankAccount(1000)
acc.deposit(500)
acc.withDraw(2500)
acc.show_balance()      



# inhertance

class Animal:
   def speak(self):
      print("Animal speaks")

class Dog(Animal):
   def bark(self):
      print("Dog bark")    

dog = Dog()
dog.speak() # I've used child class to access parent class
dog.bark()


# pormolphism