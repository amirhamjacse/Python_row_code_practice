class Animal:
    def __init__(self, name, age):
        self._name = name   # Protected attribute
        self._age = age     # Protected attribute

    def speak(self):
        print(f"{self._name} says: Hello!")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Call the parent class constructor
        self._breed = breed         # Protected attribute for Dog class

    def display_info(self):
        # Accessing protected attribute from the parent class
        print(f"{self._name} is a {self._breed} and is {self._age} years old.")

# Create an object of Dog class
dog = Dog("Buddy", 5, "Golden Retriever")

# Accessing protected attribute from outside (not recommended)
print(dog._name)  # Output: Buddy (though this should be avoided)

# Use a method to access the protected attributes
dog.display_info()  # Output: Buddy is a Golden Retriever and is 5 years old.

# Call the speak method
dog.speak()  # Output: Buddy says: Hello!
