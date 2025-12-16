# ============================================
# DICTIONARY IN PYTHON - Complete Guide
# ============================================

print("=" * 50)
print("PYTHON DICTIONARY")
print("=" * 50)

# ============================================
# CREATING DICTIONARIES
# ============================================
print("\n--- Creating Dictionaries ---")

# Empty dictionary
empty_dict = {}
print(f"Empty dict: {empty_dict}")

# Dictionary with key-value pairs
student = {
    "name": "Dushyant",
    "age": 20,
    "city": "Delhi",
    "grade": "A"
}
print(f"Student: {student}")

# Mixed key types
mixed = {
    "name": "John",
    1: "one",
    (1, 2): "tuple key",
    True: "boolean key"
}
print(f"Mixed keys: {mixed}")

# Using dict() constructor
person = dict(name="Alice", age=25, city="Mumbai")
print(f"Using dict(): {person}")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_tuples = dict(pairs)
print(f"From tuples: {from_tuples}")

# Using dict.fromkeys()
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(f"fromkeys(): {default_dict}")

# ============================================
# ACCESSING DICTIONARY ELEMENTS
# ============================================
print("\n" + "=" * 50)
print("ACCESSING DICTIONARY ELEMENTS")
print("=" * 50)

student = {"name": "Dushyant", "age": 20, "city": "Delhi", "grade": "A"}
print(f"Student: {student}")

# Using key
print("\n--- Using Key ---")
print(f"student['name']: {student['name']}")
print(f"student['age']: {student['age']}")

# KeyError if key doesn't exist
print("\nAccessing non-existent key:")
try:
    print(student['email'])
except KeyError as e:
    print(f"KeyError: {e}")

# Using get() - Safe way (no error)
print("\n--- Using get() ---")
print(f"get('name'): {student.get('name')}")
print(f"get('email'): {student.get('email')}")  # Returns None
print(f"get('email', 'N/A'): {student.get('email', 'N/A')}")  # Default value

# ============================================
# DICTIONARY METHODS
# ============================================
print("\n" + "=" * 50)
print("DICTIONARY METHODS")
print("=" * 50)

# 1. keys() - Get all keys
print("\n--- 1. keys() ---")
student = {"name": "Dushyant", "age": 20, "city": "Delhi"}
print(f"Dict: {student}")
print(f"keys(): {student.keys()}")
print(f"As list: {list(student.keys())}")

# 2. values() - Get all values
print("\n--- 2. values() ---")
print(f"values(): {student.values()}")
print(f"As list: {list(student.values())}")

# 3. items() - Get all key-value pairs
print("\n--- 3. items() ---")
print(f"items(): {student.items()}")
print(f"As list: {list(student.items())}")

# 4. get() - Get value by key (safe)
print("\n--- 4. get() ---")
print(f"get('name'): {student.get('name')}")
print(f"get('email'): {student.get('email')}")
print(f"get('email', 'Not Found'): {student.get('email', 'Not Found')}")

# 5. update() - Update/Add multiple items
print("\n--- 5. update() ---")
student = {"name": "Dushyant", "age": 20}
print(f"Before: {student}")
student.update({"age": 21, "city": "Delhi", "grade": "A"})
print(f"After update(): {student}")

# Update with keyword arguments
student.update(email="dushyant@email.com")
print(f"After update(email=...): {student}")

# 6. pop() - Remove and return value
print("\n--- 6. pop() ---")
student = {"name": "Dushyant", "age": 20, "city": "Delhi"}
print(f"Before: {student}")
removed = student.pop("city")
print(f"pop('city') returned: {removed}")
print(f"After: {student}")

# pop() with default value
removed = student.pop("email", "Key not found")
print(f"pop('email', 'Key not found'): {removed}")

# 7. popitem() - Remove and return last item
print("\n--- 7. popitem() ---")
student = {"name": "Dushyant", "age": 20, "city": "Delhi"}
print(f"Before: {student}")
last_item = student.popitem()
print(f"popitem() returned: {last_item}")
print(f"After: {student}")

# 8. setdefault() - Get or set default
print("\n--- 8. setdefault() ---")
student = {"name": "Dushyant", "age": 20}
print(f"Before: {student}")

# Key exists - returns existing value
result = student.setdefault("name", "Unknown")
print(f"setdefault('name', 'Unknown'): {result}")

# Key doesn't exist - sets and returns default
result = student.setdefault("city", "Delhi")
print(f"setdefault('city', 'Delhi'): {result}")
print(f"After: {student}")

# 9. clear() - Remove all items
print("\n--- 9. clear() ---")
temp = {"a": 1, "b": 2, "c": 3}
print(f"Before: {temp}")
temp.clear()
print(f"After clear(): {temp}")

# 10. copy() - Create shallow copy
print("\n--- 10. copy() ---")
original = {"name": "Dushyant", "age": 20}
copied = original.copy()
copied["age"] = 25
print(f"Original: {original}")
print(f"Copied: {copied}")

# 11. fromkeys() - Create dict with keys
print("\n--- 11. fromkeys() ---")
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys)
print(f"fromkeys({keys}): {new_dict}")
new_dict = dict.fromkeys(keys, "N/A")
print(f"fromkeys({keys}, 'N/A'): {new_dict}")

# ============================================
# MODIFYING DICTIONARIES
# ============================================
print("\n" + "=" * 50)
print("MODIFYING DICTIONARIES")
print("=" * 50)

student = {"name": "Dushyant", "age": 20}
print(f"Original: {student}")

# Add new key-value
print("\n--- Add New Item ---")
student["city"] = "Delhi"
print(f"After adding 'city': {student}")

# Update existing value
print("\n--- Update Existing ---")
student["age"] = 21
print(f"After updating 'age': {student}")

# Delete item
print("\n--- Delete Item ---")
del student["city"]
print(f"After del student['city']: {student}")

# ============================================
# DICTIONARY OPERATIONS
# ============================================
print("\n" + "=" * 50)
print("DICTIONARY OPERATIONS")
print("=" * 50)

student = {"name": "Dushyant", "age": 20, "city": "Delhi"}

# Length
print("\n--- Length ---")
print(f"len({student}): {len(student)}")

# Membership (checks keys only)
print("\n--- Membership (in) ---")
print(f"'name' in student: {'name' in student}")
print(f"'email' in student: {'email' in student}")
print(f"'Dushyant' in student: {'Dushyant' in student}")  # False - checks keys!

# Check in values
print(f"'Dushyant' in student.values(): {'Dushyant' in student.values()}")

# ============================================
# LOOPING THROUGH DICTIONARIES
# ============================================
print("\n" + "=" * 50)
print("LOOPING THROUGH DICTIONARIES")
print("=" * 50)

student = {"name": "Dushyant", "age": 20, "city": "Delhi"}

# Loop through keys (default)
print("\n--- Loop through Keys ---")
for key in student:
    print(f"  {key}")

# Loop through values
print("\n--- Loop through Values ---")
for value in student.values():
    print(f"  {value}")

# Loop through key-value pairs
print("\n--- Loop through Items ---")
for key, value in student.items():
    print(f"  {key}: {value}")

# ============================================
# DICTIONARY COMPREHENSION
# ============================================
print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSION")
print("=" * 50)

# Basic
print("\n--- Basic ---")
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
print("\n--- With Condition ---")
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From two lists
print("\n--- From Two Lists ---")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
name_age = {name: age for name, age in zip(names, ages)}
print(f"Name-Age: {name_age}")

# Swap keys and values
print("\n--- Swap Keys and Values ---")
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Swapped: {swapped}")

# Transform values
print("\n--- Transform Values ---")
prices = {"apple": 100, "banana": 50, "cherry": 200}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(f"Original prices: {prices}")
print(f"10% discount: {discounted}")

# ============================================
# NESTED DICTIONARIES
# ============================================
print("\n" + "=" * 50)
print("NESTED DICTIONARIES")
print("=" * 50)

# Create nested dictionary
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "marks": {"math": 85, "science": 90}
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "marks": {"math": 78, "science": 82}
    }
}

print("Students Dictionary:")
for student_id, details in students.items():
    print(f"\n  {student_id}:")
    for key, value in details.items():
        print(f"    {key}: {value}")

# Accessing nested values
print(f"\nStudent1's name: {students['student1']['name']}")
print(f"Student2's math marks: {students['student2']['marks']['math']}")

# ============================================
# MERGING DICTIONARIES
# ============================================
print("\n" + "=" * 50)
print("MERGING DICTIONARIES")
print("=" * 50)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update()
print("\n--- Using update() ---")
merged1 = dict1.copy()
merged1.update(dict2)
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"Merged: {merged1}")

# Using ** unpacking
print("\n--- Using ** Unpacking ---")
merged2 = {**dict1, **dict2}
print(f"Merged: {merged2}")

# Using | operator (Python 3.9+)
print("\n--- Using | Operator (Python 3.9+) ---")
merged3 = dict1 | dict2
print(f"Merged: {merged3}")

# ============================================
# PRACTICAL EXAMPLE
# ============================================
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: STUDENT MANAGEMENT")
print("=" * 50)

# Student management using dictionary
class StudentManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, roll_no, name, marks):
        self.students[roll_no] = {"name": name, "marks": marks}
        print(f"Added: {name} (Roll: {roll_no})")
    
    def get_student(self, roll_no):
        return self.students.get(roll_no, "Student not found")
    
    def update_marks(self, roll_no, marks):
        if roll_no in self.students:
            self.students[roll_no]["marks"] = marks
            print(f"Updated marks for Roll {roll_no}")
        else:
            print("Student not found")
    
    def get_topper(self):
        if not self.students:
            return None
        return max(self.students.items(), 
                   key=lambda x: x[1]["marks"])
    
    def display_all(self):
        print("\nAll Students:")
        print("-" * 40)
        for roll, data in self.students.items():
            print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")

# Using the class
manager = StudentManager()
manager.add_student(101, "Dushyant", 85)
manager.add_student(102, "Alice", 92)
manager.add_student(103, "Bob", 78)

manager.display_all()

print(f"\nGet student 102: {manager.get_student(102)}")

topper_roll, topper_data = manager.get_topper()
print(f"Topper: {topper_data['name']} (Roll: {topper_roll}, Marks: {topper_data['marks']})")

print("\n" + "=" * 50)
print("END OF DICTIONARY GUIDE")
print("=" * 50)
