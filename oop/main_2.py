# main_2.py (Provided for Testing)
from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # A list containing instances of different shape classes.
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Iterating over the list and calling the area() method on each object.
    # This demonstrates Polymorphism: the same method call (shape.area())
    # executes different code based on the object's type (Rectangle or Circle).
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()