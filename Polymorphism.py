# Polymorphism in Python

"""
DEFINITION:
Polymorphism is a fundamental concept of Object-Oriented Programming (OOP) that means 
"many forms". It allows objects of different classes to be treated as objects of a 
common parent class. The same method name can behave differently based on the object 
that calls it.

Types of Polymorphism:
1. Compile-time Polymorphism (Method Overloading) - Same method name with different parameters
   Note: Python doesn't support traditional method overloading, but we can achieve it using default arguments
   
2. Run-time Polymorphism (Method Overriding) - Child class provides different implementation 
   of a method that is already defined in parent class

Ways to achieve Polymorphism in Python:
- Method Overriding
- Duck Typing
- Operator Overloading
- Function Polymorphism (len(), +, etc.)

Real-world Analogy:
The word "speak" - A dog speaks by barking, a cat speaks by meowing, a human speaks words.
Same action name, different behaviors based on who performs it.
"""

# Example: Shape Calculator using Polymorphism

# Parent Class
class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def display_info(self):
        print(f"Shape: {self.name}")


# Child Class 1 - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    # Method Overriding - Same method name, different implementation
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def display_info(self):
        super().display_info()
        print(f"Length: {self.length}, Width: {self.width}")


# Child Class 2 - Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        self.pi = 3.14159
    
    # Method Overriding
    def area(self):
        return self.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * self.pi * self.radius
    
    def display_info(self):
        super().display_info()
        print(f"Radius: {self.radius}")


# Child Class 3 - Triangle
class Triangle(Shape):
    def __init__(self, side1, side2, side3, height):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
        self.base = side1
    
    # Method Overriding
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def display_info(self):
        super().display_info()
        print(f"Sides: {self.side1}, {self.side2}, {self.side3}")


# Function demonstrating Polymorphism
# Same function works with different shape objects
def calculate_shape(shape):
    """This function accepts any shape object and calls its methods"""
    shape.display_info()
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")


# Main Program
print("=== Polymorphism Example: Shape Calculator ===\n")

# Creating objects of different classes
rectangle = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(3, 4, 5, 4)

# Storing different objects in a list
shapes = [rectangle, circle, triangle]

# Polymorphism in action - Same method call, different behavior
print("--- Using Loop (Polymorphism) ---\n")
for shape in shapes:
    calculate_shape(shape)
    print()

# Duck Typing Example
print("--- Duck Typing Example ---")
print("If it walks like a duck and quacks like a duck, it's a duck!")
print("Python doesn't check the type, it checks if the method exists.\n")

# Any object with area() and perimeter() methods will work
class Square:  # Not inheriting from Shape
    def __init__(self, side):
        self.name = "Square"
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
    def display_info(self):
        print(f"Shape: {self.name}")
        print(f"Side: {self.side}")

square = Square(6)
calculate_shape(square)  # Works due to Duck Typing!
