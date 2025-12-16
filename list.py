# ============================================
# LIST IN PYTHON - Complete Guide
# ============================================

print("=" * 50)
print("PYTHON LISTS")
print("=" * 50)

# Creating Lists
print("\n--- Creating Lists ---")
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed types: {mixed}")
print(f"Nested list: {nested}")

# List using list() constructor
print(f"From string: {list('Python')}")
print(f"From range: {list(range(1, 6))}")

# ============================================
# ACCESSING LIST ELEMENTS
# ============================================
print("\n" + "=" * 50)
print("ACCESSING LIST ELEMENTS")
print("=" * 50)

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"List: {colors}")

# Indexing (0-based)
print("\n--- Positive Indexing ---")
print(f"colors[0]: {colors[0]}")   # First element
print(f"colors[2]: {colors[2]}")   # Third element
print(f"colors[-1]: {colors[-1]}") # Last element
print(f"colors[-2]: {colors[-2]}") # Second last

# Slicing
print("\n--- Slicing [start:stop:step] ---")
print(f"colors[1:4]: {colors[1:4]}")     # Index 1 to 3
print(f"colors[:3]: {colors[:3]}")       # First 3 elements
print(f"colors[2:]: {colors[2:]}")       # From index 2 to end
print(f"colors[::2]: {colors[::2]}")     # Every 2nd element
print(f"colors[::-1]: {colors[::-1]}")   # Reversed list

# ============================================
# LIST METHODS
# ============================================
print("\n" + "=" * 50)
print("LIST METHODS")
print("=" * 50)

# 1. append() - Add element at end
print("\n--- 1. append() ---")
fruits = ["apple", "banana"]
print(f"Original: {fruits}")
fruits.append("cherry")
print(f"After append('cherry'): {fruits}")

# 2. insert() - Add element at specific position
print("\n--- 2. insert() ---")
fruits.insert(1, "mango")
print(f"After insert(1, 'mango'): {fruits}")

# 3. extend() - Add multiple elements
print("\n--- 3. extend() ---")
fruits.extend(["grape", "orange"])
print(f"After extend(['grape', 'orange']): {fruits}")

# 4. remove() - Remove first occurrence of value
print("\n--- 4. remove() ---")
fruits.remove("mango")
print(f"After remove('mango'): {fruits}")

# 5. pop() - Remove and return element
print("\n--- 5. pop() ---")
nums = [10, 20, 30, 40, 50]
print(f"Original: {nums}")
popped = nums.pop()       # Remove last
print(f"pop() returned: {popped}, List: {nums}")
popped = nums.pop(1)      # Remove at index 1
print(f"pop(1) returned: {popped}, List: {nums}")

# 6. clear() - Remove all elements
print("\n--- 6. clear() ---")
temp = [1, 2, 3]
print(f"Before clear: {temp}")
temp.clear()
print(f"After clear(): {temp}")

# 7. index() - Find index of element
print("\n--- 7. index() ---")
letters = ['a', 'b', 'c', 'd', 'b', 'e']
print(f"List: {letters}")
print(f"index('c'): {letters.index('c')}")
print(f"index('b', 2): {letters.index('b', 2)}")  # Start search from index 2

# 8. count() - Count occurrences
print("\n--- 8. count() ---")
nums = [1, 2, 2, 3, 2, 4, 2]
print(f"List: {nums}")
print(f"count(2): {nums.count(2)}")

# 9. sort() - Sort list in place
print("\n--- 9. sort() ---")
numbers = [64, 25, 12, 22, 11]
print(f"Original: {numbers}")
numbers.sort()
print(f"After sort(): {numbers}")
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# Sort strings
words = ["banana", "Apple", "cherry", "Date"]
words.sort()
print(f"Sorted words: {words}")
words.sort(key=str.lower)  # Case-insensitive sort
print(f"Case-insensitive: {words}")

# 10. sorted() - Returns new sorted list
print("\n--- 10. sorted() (built-in function) ---")
original = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(original)
print(f"Original: {original}")
print(f"sorted(): {sorted_list}")

# 11. reverse() - Reverse list in place
print("\n--- 11. reverse() ---")
nums = [1, 2, 3, 4, 5]
print(f"Original: {nums}")
nums.reverse()
print(f"After reverse(): {nums}")

# 12. copy() - Create shallow copy
print("\n--- 12. copy() ---")
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print(f"Original: {original}")
print(f"Copied: {copied}")

# ============================================
# LIST OPERATIONS
# ============================================
print("\n" + "=" * 50)
print("LIST OPERATIONS")
print("=" * 50)

# Concatenation
print("\n--- Concatenation (+) ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"{list1} + {list2} = {list1 + list2}")

# Repetition
print("\n--- Repetition (*) ---")
print(f"[1, 2] * 3 = {[1, 2] * 3}")

# Length
print("\n--- Length ---")
items = ["a", "b", "c", "d"]
print(f"len({items}) = {len(items)}")

# Membership
print("\n--- Membership (in, not in) ---")
print(f"'b' in {items}: {'b' in items}")
print(f"'z' not in {items}: {'z' not in items}")

# Min, Max, Sum
print("\n--- Min, Max, Sum ---")
nums = [5, 2, 8, 1, 9]
print(f"List: {nums}")
print(f"min(): {min(nums)}")
print(f"max(): {max(nums)}")
print(f"sum(): {sum(nums)}")

# ============================================
# LIST COMPREHENSION
# ============================================
print("\n" + "=" * 50)
print("LIST COMPREHENSION")
print("=" * 50)

# Basic
print("\n--- Basic ---")
squares = [x**2 for x in range(1, 6)]
print(f"Squares 1-5: {squares}")

# With condition
print("\n--- With Condition ---")
even_nums = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers 0-9: {even_nums}")

# With if-else
print("\n--- With if-else ---")
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(f"Labels: {labels}")

# Nested comprehension
print("\n--- Nested ---")
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Flattening nested list
print("\n--- Flatten Nested List ---")
nested = [[1, 2], [3, 4], [5, 6]]
flat = [num for sublist in nested for num in sublist]
print(f"Nested: {nested}")
print(f"Flattened: {flat}")

# ============================================
# MODIFYING LISTS
# ============================================
print("\n" + "=" * 50)
print("MODIFYING LISTS")
print("=" * 50)

# Change single element
print("\n--- Change Single Element ---")
colors = ["red", "green", "blue"]
print(f"Original: {colors}")
colors[1] = "yellow"
print(f"After colors[1] = 'yellow': {colors}")

# Change range of elements
print("\n--- Change Multiple Elements ---")
nums = [1, 2, 3, 4, 5]
print(f"Original: {nums}")
nums[1:4] = [20, 30, 40]
print(f"After nums[1:4] = [20, 30, 40]: {nums}")

# Delete elements
print("\n--- Delete Elements ---")
items = ['a', 'b', 'c', 'd', 'e']
print(f"Original: {items}")
del items[2]
print(f"After del items[2]: {items}")
del items[1:3]
print(f"After del items[1:3]: {items}")

# ============================================
# LOOPING THROUGH LISTS
# ============================================
print("\n" + "=" * 50)
print("LOOPING THROUGH LISTS")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]

# Simple loop
print("\n--- Simple Loop ---")
for fruit in fruits:
    print(f"  {fruit}")

# With index
print("\n--- With enumerate() ---")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# With enumerate starting from 1
print("\n--- enumerate with start=1 ---")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# Loop with range
print("\n--- Using range() ---")
for i in range(len(fruits)):
    print(f"  fruits[{i}] = {fruits[i]}")

# ============================================
# USEFUL TIPS
# ============================================
print("\n" + "=" * 50)
print("USEFUL TIPS")
print("=" * 50)

# Swap elements
print("\n--- Swap Elements ---")
a, b = 10, 20
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After: a={a}, b={b}")

# Unpack list
print("\n--- Unpack List ---")
nums = [1, 2, 3]
x, y, z = nums
print(f"List: {nums}")
print(f"Unpacked: x={x}, y={y}, z={z}")

# Unpack with *
print("\n--- Unpack with * ---")
nums = [1, 2, 3, 4, 5]
first, *middle, last = nums
print(f"List: {nums}")
print(f"first={first}, middle={middle}, last={last}")

# Check if list is empty
print("\n--- Check Empty List ---")
empty = []
if not empty:
    print("List is empty!")

# Get unique elements (preserve order)
print("\n--- Unique Elements ---")
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(dict.fromkeys(nums))
print(f"Original: {nums}")
print(f"Unique: {unique}")

print("\n" + "=" * 50)
print("END OF LIST GUIDE")
print("=" * 50)
