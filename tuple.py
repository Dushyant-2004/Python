# ============================================
# TUPLE IN PYTHON - Complete Guide
# ============================================

print("=" * 50)
print("PYTHON TUPLES")
print("=" * 50)

# ============================================
# CREATING TUPLES
# ============================================
print("\n--- Creating Tuples ---")

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with elements
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True, None)
nested = ((1, 2), (3, 4), (5, 6))

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed types: {mixed}")
print(f"Nested tuple: {nested}")

# Single element tuple (MUST have comma)
single = (5,)      # This is a tuple
not_tuple = (5)    # This is just an integer
print(f"Single element tuple: {single}, Type: {type(single)}")
print(f"Without comma: {not_tuple}, Type: {type(not_tuple)}")

# Tuple without parentheses (tuple packing)
packed = 1, 2, 3
print(f"Packed tuple: {packed}, Type: {type(packed)}")

# Using tuple() constructor
from_list = tuple([1, 2, 3])
from_string = tuple("Python")
from_range = tuple(range(1, 6))
print(f"From list: {from_list}")
print(f"From string: {from_string}")
print(f"From range: {from_range}")

# ============================================
# TUPLE VS LIST - KEY DIFFERENCE
# ============================================
print("\n" + "=" * 50)
print("TUPLE VS LIST")
print("=" * 50)

print("""
| Feature        | Tuple              | List               |
|----------------|--------------------|--------------------|
| Syntax         | (1, 2, 3)          | [1, 2, 3]          |
| Mutability     | Immutable          | Mutable            |
| Methods        | count(), index()   | Many methods       |
| Performance    | Faster             | Slower             |
| Use Case       | Fixed data         | Dynamic data       |
| Hashable       | Yes (if elements)  | No                 |
""")

# Demonstrating immutability
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple}")
print("Trying to change element... my_tuple[0] = 10")
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")

# ============================================
# ACCESSING TUPLE ELEMENTS
# ============================================
print("\n" + "=" * 50)
print("ACCESSING TUPLE ELEMENTS")
print("=" * 50)

colors = ("red", "green", "blue", "yellow", "purple")
print(f"Tuple: {colors}")

# Positive Indexing
print("\n--- Positive Indexing ---")
print(f"colors[0]: {colors[0]}")   # First element
print(f"colors[2]: {colors[2]}")   # Third element

# Negative Indexing
print("\n--- Negative Indexing ---")
print(f"colors[-1]: {colors[-1]}") # Last element
print(f"colors[-2]: {colors[-2]}") # Second last

# Slicing
print("\n--- Slicing [start:stop:step] ---")
print(f"colors[1:4]: {colors[1:4]}")     # Index 1 to 3
print(f"colors[:3]: {colors[:3]}")       # First 3 elements
print(f"colors[2:]: {colors[2:]}")       # From index 2 to end
print(f"colors[::2]: {colors[::2]}")     # Every 2nd element
print(f"colors[::-1]: {colors[::-1]}")   # Reversed tuple

# Accessing nested tuple
print("\n--- Accessing Nested Tuple ---")
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"Nested: {nested}")
print(f"nested[1]: {nested[1]}")
print(f"nested[1][2]: {nested[1][2]}")

# ============================================
# TUPLE METHODS (Only 2!)
# ============================================
print("\n" + "=" * 50)
print("TUPLE METHODS")
print("=" * 50)

# Tuples have only 2 methods because they are immutable

# 1. count() - Count occurrences of a value
print("\n--- 1. count() ---")
nums = (1, 2, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {nums}")
print(f"count(2): {nums.count(2)}")
print(f"count(5): {nums.count(5)}")
print(f"count(10): {nums.count(10)}")

# Another example
letters = ('a', 'b', 'a', 'c', 'a', 'd', 'a')
print(f"\nTuple: {letters}")
print(f"count('a'): {letters.count('a')}")

# 2. index() - Find index of first occurrence
print("\n--- 2. index() ---")
fruits = ("apple", "banana", "cherry", "banana", "date")
print(f"Tuple: {fruits}")
print(f"index('banana'): {fruits.index('banana')}")
print(f"index('cherry'): {fruits.index('cherry')}")

# index() with start and stop parameters
print(f"index('banana', 2): {fruits.index('banana', 2)}")  # Start search from index 2

# Error handling for index()
print("\nSearching for element not in tuple:")
try:
    fruits.index('mango')
except ValueError as e:
    print(f"Error: {e}")

# ============================================
# TUPLE OPERATIONS
# ============================================
print("\n" + "=" * 50)
print("TUPLE OPERATIONS")
print("=" * 50)

# Concatenation
print("\n--- Concatenation (+) ---")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(f"{tuple1} + {tuple2} = {result}")

# Repetition
print("\n--- Repetition (*) ---")
t = (1, 2)
print(f"{t} * 3 = {t * 3}")

# Length
print("\n--- Length ---")
items = ("a", "b", "c", "d")
print(f"len({items}) = {len(items)}")

# Membership
print("\n--- Membership (in, not in) ---")
print(f"'b' in {items}: {'b' in items}")
print(f"'z' not in {items}: {'z' not in items}")

# Min, Max, Sum
print("\n--- Min, Max, Sum ---")
nums = (5, 2, 8, 1, 9)
print(f"Tuple: {nums}")
print(f"min(): {min(nums)}")
print(f"max(): {max(nums)}")
print(f"sum(): {sum(nums)}")

# Comparison
print("\n--- Comparison ---")
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (1, 2, 4)
print(f"t1 = {t1}")
print(f"t2 = {t2}")
print(f"t3 = {t3}")
print(f"t1 == t2: {t1 == t2}")
print(f"t1 == t3: {t1 == t3}")
print(f"t1 < t3: {t1 < t3}")

# ============================================
# TUPLE UNPACKING
# ============================================
print("\n" + "=" * 50)
print("TUPLE UNPACKING")
print("=" * 50)

# Basic unpacking
print("\n--- Basic Unpacking ---")
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Tuple: {coordinates}")
print(f"x = {x}, y = {y}, z = {z}")

# Unpacking with *
print("\n--- Unpacking with * ---")
nums = (1, 2, 3, 4, 5, 6)
first, *middle, last = nums
print(f"Tuple: {nums}")
print(f"first = {first}")
print(f"middle = {middle}")  # This becomes a list
print(f"last = {last}")

# Swap values using unpacking
print("\n--- Swap Values ---")
a, b = 10, 20
print(f"Before: a = {a}, b = {b}")
a, b = b, a
print(f"After: a = {a}, b = {b}")

# Unpacking in function return
print("\n--- Function Return Unpacking ---")
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max((5, 2, 8, 1, 9))
minimum, maximum = result
print(f"Result tuple: {result}")
print(f"Min: {minimum}, Max: {maximum}")

# Unpacking in loop
print("\n--- Unpacking in Loop ---")
students = (("Alice", 85), ("Bob", 92), ("Charlie", 78))
print("Students:")
for name, score in students:
    print(f"  {name}: {score}%")

# ============================================
# CONVERTING TUPLES
# ============================================
print("\n" + "=" * 50)
print("CONVERTING TUPLES")
print("=" * 50)

# Tuple to List (to modify)
print("\n--- Tuple to List ---")
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(f"Tuple: {my_tuple}")
print(f"List: {my_list}")

# Modify and convert back
my_list.append(6)
my_tuple = tuple(my_list)
print(f"Modified Tuple: {my_tuple}")

# Tuple to String
print("\n--- Tuple to String ---")
chars = ('P', 'y', 't', 'h', 'o', 'n')
string = ''.join(chars)
print(f"Tuple: {chars}")
print(f"String: {string}")

# Tuple to Set (removes duplicates)
print("\n--- Tuple to Set ---")
nums = (1, 2, 2, 3, 3, 3, 4)
unique = set(nums)
print(f"Tuple: {nums}")
print(f"Set: {unique}")

# ============================================
# TUPLE AS DICTIONARY KEY
# ============================================
print("\n" + "=" * 50)
print("TUPLE AS DICTIONARY KEY")
print("=" * 50)

# Tuples can be dictionary keys (because immutable)
print("\n--- Tuple as Dict Key ---")
locations = {
    (28.6139, 77.2090): "New Delhi",
    (19.0760, 72.8777): "Mumbai",
    (13.0827, 80.2707): "Chennai"
}

print("Coordinates Dictionary:")
for coords, city in locations.items():
    print(f"  {coords}: {city}")

# Lists CANNOT be dictionary keys
print("\nTrying list as dict key...")
try:
    bad_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"Error: {e}")

# ============================================
# NAMED TUPLES (Advanced)
# ============================================
print("\n" + "=" * 50)
print("NAMED TUPLES")
print("=" * 50)

from collections import namedtuple

# Create a named tuple class
Student = namedtuple('Student', ['name', 'age', 'grade'])

# Create instances
student1 = Student("Alice", 20, "A")
student2 = Student(name="Bob", age=22, grade="B")

print(f"Student 1: {student1}")
print(f"Student 2: {student2}")

# Access by name or index
print(f"\nAccess by name: {student1.name}")
print(f"Access by index: {student1[0]}")

# Named tuple methods
print(f"\n_fields: {Student._fields}")
print(f"_asdict(): {student1._asdict()}")

# ============================================
# PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Return multiple values from function
print("\n--- Example 1: Multiple Return Values ---")
def calculate_stats(numbers):
    """Returns tuple of (count, sum, average, min, max)"""
    count = len(numbers)
    total = sum(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    return count, total, average, minimum, maximum

nums = (10, 20, 30, 40, 50)
count, total, avg, min_val, max_val = calculate_stats(nums)
print(f"Numbers: {nums}")
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Average: {avg}")
print(f"Min: {min_val}")
print(f"Max: {max_val}")

# Example 2: Tuple for fixed configuration
print("\n--- Example 2: Fixed Configuration ---")
RGB_RED = (255, 0, 0)
RGB_GREEN = (0, 255, 0)
RGB_BLUE = (0, 0, 255)

def display_color(color_tuple):
    r, g, b = color_tuple
    print(f"R: {r}, G: {g}, B: {b}")

print("Red:", end=" ")
display_color(RGB_RED)
print("Green:", end=" ")
display_color(RGB_GREEN)

# Example 3: Enumerate returns tuples
print("\n--- Example 3: Enumerate Returns Tuples ---")
fruits = ("apple", "banana", "cherry")
for item in enumerate(fruits, start=1):
    print(f"  {item} -> Index: {item[0]}, Value: {item[1]}")

# Example 4: zip() returns tuples
print("\n--- Example 4: zip() Returns Tuples ---")
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
for pair in zip(names, ages):
    print(f"  {pair}")

print("\n" + "=" * 50)
print("END OF TUPLE GUIDE")
print("=" * 50)
