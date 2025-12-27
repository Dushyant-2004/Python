# ============================================
# ARRAYS IN PYTHON - Complete Guide
# ============================================
# In Python, we use the 'array' module for arrays or 'numpy' for advanced arrays
# Arrays store elements of the SAME data type (unlike lists)

from array import array

# ============================================
# CREATING AN ARRAY
# ============================================
# Syntax: array(typecode, [elements])
# Common typecodes: 'i' = integer, 'f' = float, 'd' = double, 'u' = unicode char

# Example: Student marks in 5 subjects
marks = array('i', [85, 92, 78, 95, 88])
print("Student Marks Array:", marks)
print("Data Type:", marks.typecode)

# ============================================
# INDEXING - Accessing Individual Elements
# ============================================
# Positive indexing: starts from 0 (left to right)
# Negative indexing: starts from -1 (right to left)

#  Index:      0    1    2    3    4
#  Marks:    [85,  92,  78,  95,  88]
#  Neg Idx:  -5   -4   -3   -2   -1

print("\n--- INDEXING ---")
print("First subject marks (index 0):", marks[0])      # Output: 85
print("Third subject marks (index 2):", marks[2])      # Output: 78
print("Last subject marks (index -1):", marks[-1])     # Output: 88
print("Second last marks (index -2):", marks[-2])      # Output: 95

# ============================================
# SLICING - Accessing Multiple Elements
# ============================================
# Syntax: array[start:stop:step]
# start = starting index (inclusive)
# stop = ending index (exclusive)
# step = increment value (default is 1)

print("\n--- SLICING ---")
print("Marks from index 1 to 3:", marks[1:4])          # Output: array('i', [92, 78, 95])
print("First 3 subjects:", marks[:3])                   # Output: array('i', [85, 92, 78])
print("Last 3 subjects:", marks[2:])                    # Output: array('i', [78, 95, 88])
print("All marks:", marks[:])                           # Output: array('i', [85, 92, 78, 95, 88])
print("Every 2nd element:", marks[::2])                 # Output: array('i', [85, 78, 88])
print("Reverse array:", marks[::-1])                    # Output: array('i', [88, 95, 78, 92, 85])
print("From index 1 to 4, step 2:", marks[1:5:2])       # Output: array('i', [92, 95])

# ============================================
# ARRAY PROPERTIES & METHODS
# ============================================

print("\n--- ARRAY PROPERTIES ---")
print("Length of array:", len(marks))                   # Output: 5
print("Buffer info:", marks.buffer_info())              # (memory address, length)
print("Item size (bytes):", marks.itemsize)             # Size of one element

# ============================================
# MODIFYING ELEMENTS
# ============================================
print("\n--- MODIFYING ELEMENTS ---")
marks[2] = 80                                           # Change 78 to 80
print("After modifying index 2:", marks)

# ============================================
# ADDING ELEMENTS
# ============================================
print("\n--- ADDING ELEMENTS ---")

# append() - Add single element at end
marks.append(90)
print("After append(90):", marks)

# insert() - Add element at specific position
marks.insert(1, 91)                                     # Insert 91 at index 1
print("After insert(1, 91):", marks)

# extend() - Add multiple elements
marks.extend([82, 87])
print("After extend([82, 87]):", marks)

# ============================================
# REMOVING ELEMENTS
# ============================================
print("\n--- REMOVING ELEMENTS ---")

# pop() - Remove and return element at index (default: last)
removed = marks.pop()
print("Popped element:", removed)
print("After pop():", marks)

removed = marks.pop(1)                                  # Remove element at index 1
print("Popped element at index 1:", removed)
print("After pop(1):", marks)

# remove() - Remove first occurrence of value
marks.remove(80)
print("After remove(80):", marks)

# ============================================
# SEARCHING ELEMENTS
# ============================================
print("\n--- SEARCHING ELEMENTS ---")
print("Index of 95:", marks.index(95))                  # Find index of value
print("Count of 85:", marks.count(85))                  # Count occurrences

# ============================================
# OTHER USEFUL METHODS
# ============================================
print("\n--- OTHER METHODS ---")

# reverse() - Reverse array in place
marks.reverse()
print("After reverse():", marks)

# Convert to list
marks_list = marks.tolist()
print("Converted to list:", marks_list)

# ============================================
# ARRAY vs LIST COMPARISON
# ============================================
print("\n--- ARRAY vs LIST ---")
print("""
| Feature        | Array                    | List                     |
|----------------|--------------------------|--------------------------|
| Data Type      | Same type only           | Different types allowed  |
| Memory         | More efficient           | Less efficient           |
| Speed          | Faster for numeric ops   | Slower for numeric ops   |
| Flexibility    | Less flexible            | More flexible            |
| Import needed  | Yes (array module)       | No (built-in)            |
""")

# ============================================
# PRACTICAL EXAMPLE: Temperature Analysis
# ============================================
print("=" * 50)
print("PRACTICAL EXAMPLE: Weekly Temperature Analysis")
print("=" * 50)

# Daily temperatures for a week (in Celsius)
temperatures = array('f', [28.5, 30.2, 29.8, 31.5, 32.0, 27.5, 29.0])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("\nWeekly Temperatures:", temperatures)

# Indexing - Get specific day's temperature
print(f"\nMonday's temperature: {temperatures[0]}°C")
print(f"Friday's temperature: {temperatures[4]}°C")
print(f"Sunday's temperature: {temperatures[-1]}°C")

# Slicing - Get weekday vs weekend temperatures
weekday_temps = temperatures[:5]
weekend_temps = temperatures[5:]
print(f"\nWeekday temperatures: {weekday_temps.tolist()}")
print(f"Weekend temperatures: {weekend_temps.tolist()}")

# Analysis
print(f"\nAverage temperature: {sum(temperatures)/len(temperatures):.2f}°C")
print(f"Highest temperature: {max(temperatures)}°C")
print(f"Lowest temperature: {min(temperatures)}°C")

# Mid-week temperatures (Tue to Thu)
midweek = temperatures[1:4]
print(f"Mid-week temps (Tue-Thu): {midweek.tolist()}")

# Alternate days
alternate = temperatures[::2]
print(f"Alternate day temps: {alternate.tolist()}")
