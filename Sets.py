# ============================================
# SETS IN PYTHON - Complete Guide
# ============================================

print("=" * 50)
print("PYTHON SETS")
print("=" * 50)

# ============================================
# CREATING SETS
# ============================================
print("\n--- Creating Sets ---")

# Empty set (MUST use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Type of set(): {type(empty_set)}")
print(f"Type of {{}}: {type({})}")  # This is dict, not set!

# Set with elements
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
mixed = {1, "hello", 3.14, True}

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# Sets automatically remove duplicates
print("\n--- Sets Remove Duplicates ---")
with_duplicates = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"{{1, 2, 2, 3, 3, 3, 4, 4, 4, 4}} = {with_duplicates}")

# Using set() constructor
from_list = set([1, 2, 3, 4, 5])
from_string = set("hello")  # Unique characters
from_tuple = set((1, 2, 3))
print(f"From list: {from_list}")
print(f"From string 'hello': {from_string}")
print(f"From tuple: {from_tuple}")

# ============================================
# SET PROPERTIES
# ============================================
print("\n" + "=" * 50)
print("SET PROPERTIES")
print("=" * 50)

print("""
1. Unordered - No index access
2. Unique elements - No duplicates
3. Mutable - Can add/remove elements
4. Elements must be immutable (no lists/dicts)
5. Cannot contain duplicate values
""")

# No indexing allowed
print("--- No Indexing ---")
my_set = {1, 2, 3}
try:
    print(my_set[0])
except TypeError as e:
    print(f"Error: {e}")

# ============================================
# SET METHODS - ADDING ELEMENTS
# ============================================
print("\n" + "=" * 50)
print("ADDING ELEMENTS")
print("=" * 50)

# 1. add() - Add single element
print("\n--- 1. add() ---")
fruits = {"apple", "banana"}
print(f"Original: {fruits}")
fruits.add("cherry")
print(f"After add('cherry'): {fruits}")
fruits.add("apple")  # No effect - already exists
print(f"After add('apple'): {fruits}")

# 2. update() - Add multiple elements
print("\n--- 2. update() ---")
numbers = {1, 2, 3}
print(f"Original: {numbers}")
numbers.update([4, 5, 6])
print(f"After update([4, 5, 6]): {numbers}")
numbers.update({7, 8}, [9, 10])  # Multiple iterables
print(f"After update({{7, 8}}, [9, 10]): {numbers}")

# ============================================
# SET METHODS - REMOVING ELEMENTS
# ============================================
print("\n" + "=" * 50)
print("REMOVING ELEMENTS")
print("=" * 50)

# 3. remove() - Remove element (raises error if not found)
print("\n--- 3. remove() ---")
fruits = {"apple", "banana", "cherry", "mango"}
print(f"Original: {fruits}")
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

print("\nRemoving non-existent element:")
try:
    fruits.remove("grape")
except KeyError as e:
    print(f"KeyError: {e}")

# 4. discard() - Remove element (NO error if not found)
print("\n--- 4. discard() ---")
fruits = {"apple", "banana", "cherry"}
print(f"Original: {fruits}")
fruits.discard("banana")
print(f"After discard('banana'): {fruits}")
fruits.discard("grape")  # No error!
print(f"After discard('grape'): {fruits}")

# 5. pop() - Remove and return random element
print("\n--- 5. pop() ---")
numbers = {1, 2, 3, 4, 5}
print(f"Original: {numbers}")
popped = numbers.pop()
print(f"pop() returned: {popped}")
print(f"After pop(): {numbers}")

# 6. clear() - Remove all elements
print("\n--- 6. clear() ---")
temp = {1, 2, 3}
print(f"Before: {temp}")
temp.clear()
print(f"After clear(): {temp}")

# ============================================
# SET METHODS - SET OPERATIONS
# ============================================
print("\n" + "=" * 50)
print("SET OPERATIONS")
print("=" * 50)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"Set A: {A}")
print(f"Set B: {B}")

# 7. union() - All elements from both sets
print("\n--- 7. union() | ---")
print(f"A.union(B): {A.union(B)}")
print(f"A | B: {A | B}")

# 8. intersection() - Common elements
print("\n--- 8. intersection() & ---")
print(f"A.intersection(B): {A.intersection(B)}")
print(f"A & B: {A & B}")

# 9. difference() - Elements in A but not in B
print("\n--- 9. difference() - ---")
print(f"A.difference(B): {A.difference(B)}")
print(f"A - B: {A - B}")
print(f"B - A: {B - A}")

# 10. symmetric_difference() - Elements in either, but not both
print("\n--- 10. symmetric_difference() ^ ---")
print(f"A.symmetric_difference(B): {A.symmetric_difference(B)}")
print(f"A ^ B: {A ^ B}")

# Visual representation
print("\n--- Visual Representation ---")
print(f"""
    A = {A}
    B = {B}
    
    A ∪ B (union)        = {A | B}
    A ∩ B (intersection) = {A & B}
    A - B (difference)   = {A - B}
    A △ B (symmetric)    = {A ^ B}
""")

# ============================================
# SET METHODS - UPDATE OPERATIONS (In-place)
# ============================================
print("\n" + "=" * 50)
print("UPDATE OPERATIONS (In-place)")
print("=" * 50)

# 11. intersection_update() - Keep only common elements
print("\n--- 11. intersection_update() ---")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"set1: {set1}, set2: {set2}")
set1.intersection_update(set2)
print(f"After set1.intersection_update(set2): {set1}")

# 12. difference_update() - Remove elements found in other set
print("\n--- 12. difference_update() ---")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"set1: {set1}, set2: {set2}")
set1.difference_update(set2)
print(f"After set1.difference_update(set2): {set1}")

# 13. symmetric_difference_update()
print("\n--- 13. symmetric_difference_update() ---")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"set1: {set1}, set2: {set2}")
set1.symmetric_difference_update(set2)
print(f"After set1.symmetric_difference_update(set2): {set1}")

# ============================================
# SET METHODS - COMPARISON
# ============================================
print("\n" + "=" * 50)
print("SET COMPARISON METHODS")
print("=" * 50)

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}
D = {6, 7, 8}

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"D = {D}")

# 14. issubset() - Is A subset of B?
print("\n--- 14. issubset() <= ---")
print(f"A.issubset(B): {A.issubset(B)}")  # True
print(f"A <= B: {A <= B}")
print(f"B.issubset(A): {B.issubset(A)}")  # False

# 15. issuperset() - Is B superset of A?
print("\n--- 15. issuperset() >= ---")
print(f"B.issuperset(A): {B.issuperset(A)}")  # True
print(f"B >= A: {B >= A}")

# 16. isdisjoint() - No common elements?
print("\n--- 16. isdisjoint() ---")
print(f"A.isdisjoint(D): {A.isdisjoint(D)}")  # True (no common)
print(f"A.isdisjoint(B): {A.isdisjoint(B)}")  # False (has common)

# Equality
print("\n--- Equality ---")
print(f"A == C: {A == C}")  # True
print(f"A == B: {A == B}")  # False

# Proper subset/superset
print("\n--- Proper Subset/Superset ---")
print(f"A < B (proper subset): {A < B}")   # True
print(f"A < C (proper subset): {A < C}")   # False (equal)
print(f"B > A (proper superset): {B > A}") # True

# ============================================
# SET METHODS - COPY
# ============================================
print("\n" + "=" * 50)
print("COPY METHOD")
print("=" * 50)

# 17. copy() - Create shallow copy
print("\n--- 17. copy() ---")
original = {1, 2, 3, 4, 5}
copied = original.copy()
copied.add(6)
print(f"Original: {original}")
print(f"Copied: {copied}")

# ============================================
# SET OPERATIONS SUMMARY
# ============================================
print("\n" + "=" * 50)
print("SET OPERATIONS SUMMARY")
print("=" * 50)

print("""
| Operation              | Method                      | Operator |
|------------------------|-----------------------------|----------|
| Union                  | A.union(B)                  | A | B    |
| Intersection           | A.intersection(B)           | A & B    |
| Difference             | A.difference(B)             | A - B    |
| Symmetric Difference   | A.symmetric_difference(B)   | A ^ B    |
| Subset                 | A.issubset(B)               | A <= B   |
| Proper Subset          | -                           | A < B    |
| Superset               | A.issuperset(B)             | A >= B   |
| Proper Superset        | -                           | A > B    |
""")

# ============================================
# LOOPING THROUGH SETS
# ============================================
print("\n" + "=" * 50)
print("LOOPING THROUGH SETS")
print("=" * 50)

fruits = {"apple", "banana", "cherry"}
print(f"Set: {fruits}")

# Simple loop
print("\n--- Simple Loop ---")
for fruit in fruits:
    print(f"  {fruit}")

# Using enumerate
print("\n--- With enumerate() ---")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# ============================================
# SET COMPREHENSION
# ============================================
print("\n" + "=" * 50)
print("SET COMPREHENSION")
print("=" * 50)

# Basic
print("\n--- Basic ---")
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
print("\n--- With Condition ---")
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From string (unique characters)
print("\n--- Unique Characters ---")
text = "programming"
unique_chars = {char for char in text}
print(f"'{text}' unique chars: {unique_chars}")

# ============================================
# FROZEN SET (Immutable Set)
# ============================================
print("\n" + "=" * 50)
print("FROZEN SET (Immutable)")
print("=" * 50)

# Create frozen set
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen}")
print(f"Type: {type(frozen)}")

# Cannot modify
print("\nTrying to add element:")
try:
    frozen.add(6)
except AttributeError as e:
    print(f"Error: {e}")

# Frozen set operations work
print(f"\nFrozen set operations:")
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print(f"fs1: {fs1}")
print(f"fs2: {fs2}")
print(f"fs1 | fs2: {fs1 | fs2}")
print(f"fs1 & fs2: {fs1 & fs2}")

# Frozen set as dictionary key
print("\n--- Frozen Set as Dict Key ---")
my_dict = {
    frozenset([1, 2]): "Group A",
    frozenset([3, 4]): "Group B"
}
print(f"Dict with frozen set keys: {my_dict}")

# ============================================
# PRACTICAL EXAMPLE
# ============================================
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: STUDENT COURSES")
print("=" * 50)

# Students and their enrolled courses
alice_courses = {"Math", "Physics", "Chemistry", "Biology"}
bob_courses = {"Math", "Computer Science", "Physics", "English"}
charlie_courses = {"Biology", "Chemistry", "English", "History"}

print(f"Alice's courses: {alice_courses}")
print(f"Bob's courses: {bob_courses}")
print(f"Charlie's courses: {charlie_courses}")

# Common courses between Alice and Bob
print(f"\n1. Common courses (Alice & Bob):")
print(f"   {alice_courses & bob_courses}")

# All unique courses
print(f"\n2. All unique courses offered:")
all_courses = alice_courses | bob_courses | charlie_courses
print(f"   {all_courses}")

# Courses only Alice takes
print(f"\n3. Courses only Alice takes (not Bob or Charlie):")
only_alice = alice_courses - bob_courses - charlie_courses
print(f"   {only_alice}")

# Courses taken by exactly one student
print(f"\n4. Courses taken by all three:")
common_all = alice_courses & bob_courses & charlie_courses
print(f"   {common_all if common_all else 'None'}")

# Find students taking a specific course
print(f"\n5. Who takes 'Physics'?")
students = {"Alice": alice_courses, "Bob": bob_courses, "Charlie": charlie_courses}
physics_students = [name for name, courses in students.items() if "Physics" in courses]
print(f"   {physics_students}")

# ============================================
# USEFUL SET OPERATIONS
# ============================================
print("\n" + "=" * 50)
print("USEFUL SET OPERATIONS")
print("=" * 50)

# Remove duplicates from list
print("\n--- Remove Duplicates from List ---")
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_list = list(set(my_list))
print(f"Original: {my_list}")
print(f"Unique: {unique_list}")

# Check for common elements
print("\n--- Check Common Elements ---")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
has_common = bool(set(list1) & set(list2))
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"Has common elements: {has_common}")

# Find missing elements
print("\n--- Find Missing Elements ---")
required = {1, 2, 3, 4, 5}
present = {1, 2, 4}
missing = required - present
print(f"Required: {required}")
print(f"Present: {present}")
print(f"Missing: {missing}")

print("\n" + "=" * 50)
print("END OF SETS GUIDE")
print("=" * 50)
