import math

class Shape:
    """
    Base class for all geometric shapes.
    Defines the interface for the area() method.
    """
    def area(self):
        # Raises an error to ensure that derived classes implement their own
        # specific area calculation method (Method Overriding).
        raise NotImplementedError("Subclass must implement abstract method 'area'")

class Rectangle(Shape):
    """
    Derived class for a Rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        # Initialize the specific attributes for a Rectangle.
        self.length = length
        self.width = width

    def area(self):
        # Overrides the Shape.area() method.
        # Calculates and returns the area of the rectangle.
        return self.length * self.width

class Circle(Shape):
    """
    Derived class for a Circle, inheriting from Shape.
    """
    def __init__(self, radius):
        # Initialize the specific attribute for a Circle.
        self.radius = radius

    def area(self):
        # Overrides the Shape.area() method.
        # Calculates and returns the area of the circle using math.pi.
        return math.pi * (self.radius ** 2)

