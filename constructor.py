# ============================================
# CONSTRUCTOR IN PYTHON - Complete Guide
# ============================================

print("=" * 50)
print("PYTHON CONSTRUCTORS")
print("=" * 50)

# ============================================
# WHAT IS A CONSTRUCTOR?
# ============================================
print("""
A CONSTRUCTOR is a special method that is automatically called 
when an object is created. It is used to initialize the object's 
attributes (variables).

In Python, the constructor method is: __init__()

Key Points:
- Constructor name is always __init__()
- First parameter is always 'self' (reference to object)
- Called automatically when object is created
- Used to initialize object attributes
- Can take parameters to set initial values
""")

# ============================================
# TYPES OF CONSTRUCTORS
# ============================================
print("=" * 50)
print("TYPES OF CONSTRUCTORS")
print("=" * 50)

# 1. DEFAULT CONSTRUCTOR (No parameters)
print("\n--- 1. Default Constructor ---")

class Dog:
    # Default constructor - no parameters except self
    def __init__(self):
        self.name = "Unknown"
        self.breed = "Unknown"
        print("Dog object created!")
    
    def display(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

# Creating object - constructor called automatically
dog1 = Dog()
dog1.display()


# 2. PARAMETERIZED CONSTRUCTOR (With parameters)
print("\n--- 2. Parameterized Constructor ---")

class Cat:
    # Parameterized constructor
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        print(f"Cat '{name}' created!")
    
    def display(self):
        print(f"Name: {self.name}, Color: {self.color}, Age: {self.age}")

# Creating objects with parameters
cat1 = Cat("Whiskers", "White", 3)
cat1.display()

cat2 = Cat("Tom", "Gray", 5)
cat2.display()


# 3. CONSTRUCTOR WITH DEFAULT VALUES
print("\n--- 3. Constructor with Default Values ---")

class Bird:
    def __init__(self, name="Unknown", can_fly=True):
        self.name = name
        self.can_fly = can_fly
    
    def display(self):
        fly_status = "can fly" if self.can_fly else "cannot fly"
        print(f"{self.name} {fly_status}")

bird1 = Bird()  # Uses default values
bird2 = Bird("Sparrow")  # name provided, can_fly uses default
bird3 = Bird("Penguin", False)  # Both provided

bird1.display()
bird2.display()
bird3.display()


# ============================================
# COMPLETE EXAMPLE: STUDENT CLASS
# ============================================
print("\n" + "=" * 50)
print("COMPLETE EXAMPLE: STUDENT CLASS")
print("=" * 50)

class Student:
    # Class variable (shared by all objects)
    school_name = "ABC School"
    total_students = 0
    
    # Constructor
    def __init__(self, name, roll_no, marks):
        # Instance variables (unique to each object)
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = self._calculate_grade()  # Call private method
        
        # Increment class variable
        Student.total_students += 1
        
        print(f"Student '{name}' registered successfully!")
    
    # Private method (starts with _)
    def _calculate_grade(self):
        if self.marks >= 90:
            return 'A+'
        elif self.marks >= 80:
            return 'A'
        elif self.marks >= 70:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        elif self.marks >= 50:
            return 'D'
        else:
            return 'F'
    
    # Instance method
    def display(self):
        print(f"\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}")
    
    # Instance method to update marks
    def update_marks(self, new_marks):
        self.marks = new_marks
        self.grade = self._calculate_grade()
        print(f"Marks updated for {self.name}")
    
    # Class method (works with class variables)
    @classmethod
    def get_total_students(cls):
        return cls.total_students
    
    # Static method (utility function)
    @staticmethod
    def is_passing(marks):
        return marks >= 50

# Creating Student objects
print("\n--- Creating Students ---")
student1 = Student("Dushyant", 101, 85)
student2 = Student("Alice", 102, 92)
student3 = Student("Bob", 103, 45)

# Display student details
student1.display()
student2.display()
student3.display()

# Using class method
print(f"\nTotal Students: {Student.get_total_students()}")

# Using static method
print(f"\nIs 75 passing? {Student.is_passing(75)}")
print(f"Is 40 passing? {Student.is_passing(40)}")

# Update marks
print("\n--- Updating Marks ---")
student3.update_marks(55)
student3.display()


# ============================================
# SPECIAL METHODS (DUNDER/MAGIC METHODS)
# ============================================
print("\n" + "=" * 50)
print("SPECIAL METHODS (DUNDER METHODS)")
print("=" * 50)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # __str__: String representation (user-friendly)
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # __repr__: Official representation (for developers)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # __len__: Return length
    def __len__(self):
        return self.pages
    
    # __eq__: Equality comparison
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    # __lt__: Less than comparison (for sorting)
    def __lt__(self, other):
        return self.pages < other.pages
    
    # __add__: Addition operator
    def __add__(self, other):
        return self.pages + other.pages

# Creating Book objects
book1 = Book("Python Basics", "John", 200)
book2 = Book("Advanced Python", "Alice", 350)
book3 = Book("Python Basics", "John", 200)

print("\n--- String Representations ---")
print(f"str(book1): {str(book1)}")
print(f"repr(book1): {repr(book1)}")

print("\n--- Special Methods in Action ---")
print(f"len(book1): {len(book1)} pages")
print(f"book1 == book3: {book1 == book3}")
print(f"book1 == book2: {book1 == book2}")
print(f"book1 < book2: {book1 < book2}")
print(f"book1 + book2: {book1 + book2} total pages")

# Sorting using __lt__
print("\n--- Sorting Books ---")
books = [book2, book1, Book("Data Science", "Bob", 280)]
books.sort()
print("Books sorted by pages:")
for book in books:
    print(f"  {book} ({len(book)} pages)")


# ============================================
# CONSTRUCTOR WITH *args AND **kwargs
# ============================================
print("\n" + "=" * 50)
print("CONSTRUCTOR WITH *args AND **kwargs")
print("=" * 50)

class Person:
    def __init__(self, name, *hobbies, **details):
        self.name = name
        self.hobbies = hobbies  # Tuple of extra positional args
        self.details = details  # Dict of keyword args
    
    def display(self):
        print(f"\nName: {self.name}")
        print(f"Hobbies: {', '.join(self.hobbies)}")
        print("Details:")
        for key, value in self.details.items():
            print(f"  {key}: {value}")

person = Person("Dushyant", 
                "Reading", "Coding", "Gaming",  # *args
                age=20, city="Delhi", country="India")  # **kwargs
person.display()


# ============================================
# INHERITANCE AND CONSTRUCTOR
# ============================================
print("\n" + "=" * 50)
print("INHERITANCE AND CONSTRUCTOR")
print("=" * 50)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"Animal constructor called for {name}")
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor using super()
        super().__init__(name, "Dog")
        self.breed = breed
        print(f"Dog constructor called for {name}")
    
    def speak(self):
        return "Woof!"
    
    def display(self):
        print(f"Name: {self.name}, Species: {self.species}, Breed: {self.breed}")

print("\n--- Creating Dog Object ---")
dog = Dog("Buddy", "Golden Retriever")
dog.display()
print(f"Sound: {dog.speak()}")


# ============================================
# DESTRUCTOR (__del__)
# ============================================
print("\n" + "=" * 50)
print("DESTRUCTOR (__del__)")
print("=" * 50)

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        print(f"Opening file: {filename}")
    
    def __del__(self):
        print(f"Closing file: {self.filename}")

print("\n--- File Handler Example ---")
file1 = FileHandler("data.txt")
print("Working with file...")
del file1  # Explicitly delete - destructor called


# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 50)
print("CONSTRUCTOR SUMMARY")
print("=" * 50)

print("""
CONSTRUCTOR TYPES:
1. Default Constructor - __init__(self)
2. Parameterized Constructor - __init__(self, param1, param2)
3. Constructor with Default Values - __init__(self, param1="default")

SPECIAL METHODS:
| Method      | Purpose                           |
|-------------|-----------------------------------|
| __init__    | Constructor (initialize object)   |
| __del__     | Destructor (cleanup)              |
| __str__     | String representation             |
| __repr__    | Official representation           |
| __len__     | Length of object                  |
| __eq__      | Equality (==)                     |
| __lt__      | Less than (<)                     |
| __gt__      | Greater than (>)                  |
| __add__     | Addition (+)                      |
| __sub__     | Subtraction (-)                   |

KEY POINTS:
- self refers to the current instance
- super() calls parent class methods
- Class variables are shared by all instances
- Instance variables are unique to each object
""")

print("\n" + "=" * 50)
print("END OF CONSTRUCTOR GUIDE")
print("=" * 50)
