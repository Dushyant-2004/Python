# Inheritance in Python

"""
DEFINITION:
Inheritance is a fundamental concept of Object-Oriented Programming (OOP) that allows 
a class (child/derived class) to inherit attributes and methods from another class 
(parent/base class). This promotes code reusability and establishes a relationship 
between classes.

Types of Inheritance:
1. Single Inheritance - One child class inherits from one parent class
2. Multiple Inheritance - One child class inherits from multiple parent classes
3. Multilevel Inheritance - Child class inherits from a parent, which inherits from another parent
4. Hierarchical Inheritance - Multiple child classes inherit from one parent class
5. Hybrid Inheritance - Combination of two or more types of inheritance

Key Terms:
- Parent/Base/Super Class: The class being inherited from
- Child/Derived/Sub Class: The class that inherits from parent class
- super(): Function used to call parent class methods
"""

# Example: Single Inheritance - Employee Management System

# Parent Class (Base Class)
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")
    
    def work(self):
        print(f"{self.name} is working.")


# Child Class (Derived Class) - Inherits from Employee
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        # Calling parent class constructor using super()
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language  # Additional attribute
    
    # Overriding parent method
    def display_info(self):
        super().display_info()  # Call parent's display_info
        print(f"Programming Language: {self.programming_language}")
    
    # New method specific to Developer
    def code(self):
        print(f"{self.name} is coding in {self.programming_language}.")


# Another Child Class - Inherits from Employee
class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size  # Additional attribute
    
    # Overriding parent method
    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size} members")
    
    # New method specific to Manager
    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting with {self.team_size} team members.")


# Creating objects
print("=== Inheritance Example: Employee Management ===\n")

# Parent class object
print("--- General Employee ---")
emp = Employee("Rahul", "E001", 40000)
emp.display_info()
emp.work()

print("\n--- Developer (Child Class) ---")
dev = Developer("Dushyant", "D001", 60000, "Python")
dev.display_info()  # Inherited + overridden method
dev.work()          # Inherited method from parent
dev.code()          # New method in child class

print("\n--- Manager (Child Class) ---")
mgr = Manager("Priya", "M001", 80000, 10)
mgr.display_info()      # Inherited + overridden method
mgr.work()              # Inherited method from parent
mgr.conduct_meeting()   # New method in child class
