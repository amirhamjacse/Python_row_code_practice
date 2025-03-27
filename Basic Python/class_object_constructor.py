class Info:
    # use this if need parameter in class
    def __init__(self, name):
        self.name = name

    def infofunc(self, age):
        print(self.name, age)

inf = Info('Hamja')
inf.infofunc(24)

class InforMation:
    def __init__(self):
        self.name = input("Enter Your name: ")
        self.age = input("Enter Your age: ")
    
    def showinfo(self):
        print(self.name, "Your age", self.age)
        # print("Your age is: ", self.age)

obj1 = InforMation()
obj2 = InforMation()
obj1.showinfo()
obj2.showinfo()

# show the memory address of the object
# print(id(inf))


# Define a class named 'Car'
class Car:
    # Constructor to initialize the object
    def __init__(self, make, model, year):
        self.make = make      # Instance variable
        self.model = model    # Instance variable
        self.year = year      # Instance variable

    # Method to describe the car
    def describe_car(self):
        return f"{self.year} {self.make} {self.model}"

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Access method using the object
print(my_car.describe_car())  # Output: 2020 Toyota Corolla
