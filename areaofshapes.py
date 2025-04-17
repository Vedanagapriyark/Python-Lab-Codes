import math

# Base class
class Shape:
    def area(self):
        return 0

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Main program
if __name__ == "__main__":
    print("Choose a shape:")
    print("1. Rectangle")
    print("2. Circle")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        rect = Rectangle(width, height)
        print(f"Area of Rectangle: {rect.area()}")
    elif choice == "2":
        radius = float(input("Enter the radius of the circle: "))
        circ = Circle(radius)
        print(f"Area of Circle: {circ.area():.2f}")
    else:
        print("Invalid choice!")

OUTPUT:
Choose a shape:
1. Rectangle
2. Circle
Enter choice (1/2): 1
Enter the width of the rectangle: 2
Enter the height of the rectangle: 3
Area of Rectangle: 6.0
Choose a shape:
1. Rectangle
2. Circle
Enter choice (1/2): 2
Enter the radius of the circle: 3
Area of Circle: 28.27

