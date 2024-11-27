#Example of Method Overriding in Multiple Classes:
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Creating objects of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the same method on different objects
dog.sound()  # Output: Bark
cat.sound()  # Output: Meow

#Using Polymorphism with Method Overriding:
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Function that expects an Animal object
def make_animal_sound(animal: Animal):
    animal.sound()  # Calls the overridden method based on the actual object

# Passing different objects to the function
dog = Dog()
cat = Cat()

make_animal_sound(dog)  # Output: Bark
make_animal_sound(cat)  # Output: Meow
