from abc import ABC, abstractmethod

# Define an abstract class 'Shape' with an abstract method
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define a 'Rectangle' class that implements the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Define a 'Circle' class that implements the abstract method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Create objects of Rectangle and Circle
rect = Rectangle(4, 5)
circle = Circle(3)

# Access the area method from both classes
print(rect.area())  # Output: 20
print(circle.area())  # Output: 28.26
