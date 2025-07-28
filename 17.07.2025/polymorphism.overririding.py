import math

# Base class
class Shape:
    def area(self):
        return 0

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# List of shapes demonstrating polymorphism
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(10, 2)
]

# Loop to demonstrate polymorphism
for shape in shapes:
    print(f"The area is: {shape.area():.2f}")
