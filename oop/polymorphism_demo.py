import math

# Base Class
class Shape:
    def area(self):
        """Raises an error to ensure derived classes override this method."""
        raise NotImplementedError("The area() method must be implemented by subclasses.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * self.radius ** 2

# Example Usage
if __name__ == "__main__":
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(10, 5)
    circle = Circle(7)

    # Display their areas
    print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 50
    print(f"Circle Area: {circle.area():.2f}")    # Output: Circle Area: 153.94
