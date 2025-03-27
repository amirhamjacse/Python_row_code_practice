class Student:
    def __init__(self, name):
        self.name = name

    def showinfo(self):
        print(self.name)

class Students(Student):
    # if you want to use parent class's function then use
    def showinfo(self):
        return super().showinfo()
    # if you want to override then
    def showinfo(self):
        print(self.name, "method override")

obj1 = Student("Hamja")
obj1.showinfo()
obj2 = Students("Hamja")
obj2.showinfo()


# Define a parent class 'Vehicle'
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"{self.brand} {self.model} engine started!"

# Define a child class 'Car' inheriting from 'Vehicle'
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)  # Call parent constructor
        self.num_doors = num_doors

    # Method to describe the car
    def describe_car(self):
        return f"{self.brand} {self.model} with {self.num_doors} doors."

# Create an object of the Car class
my_car = Car("Toyota", "Camry", 4)

# Access methods and properties
print(my_car.start_engine())  # Output: Toyota Camry engine started!
print(my_car.describe_car())  # Output: Toyota Camry with 4 doors.
