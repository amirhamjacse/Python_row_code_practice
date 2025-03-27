# Define a parent class 'Animal'
class Animal:
    def speak(self):
        return "Some generic animal sound"

# Define a child class 'Dog' inheriting from 'Animal'
class Dog(Animal):
    def speak(self):
        return "Bark! Bark!"

# Define another child class 'Cat' inheriting from 'Animal'
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create objects of Dog and Cat
dog = Dog()
cat = Cat()

# Demonstrating polymorphism
print(dog.speak())  # Output: Bark! Bark!
print(cat.speak())  # Output: Meow!
