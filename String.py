# ============================================
# STRING METHODS AND FORMATTING IN PYTHON
# ============================================

# Sample string for demonstration
text = "  Hello, Welcome to Python Programming!  "
print("=" * 50)
print("STRING METHODS")
print("=" * 50)
print(f"Original string: '{text}'")

# 1. CASE METHODS
print("\n--- Case Methods ---")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"swapcase(): '{text.swapcase()}'")

# 2. STRIP METHODS (Remove whitespace)
print("\n--- Strip Methods ---")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")

# 3. FIND AND REPLACE
print("\n--- Find and Replace ---")
sample = "Python is awesome. Python is easy."
print(f"String: '{sample}'")
print(f"find('Python'): {sample.find('Python')}")
print(f"rfind('Python'): {sample.rfind('Python')}")
print(f"index('is'): {sample.index('is')}")
print(f"count('Python'): {sample.count('Python')}")
print(f"replace('Python', 'Java'): '{sample.replace('Python', 'Java')}'")

# 4. CHECK METHODS (Returns True/False)
print("\n--- Check Methods ---")
word = "Python3"
print(f"String: '{word}'")
print(f"isalpha(): {word.isalpha()}")
print(f"isdigit(): {word.isdigit()}")
print(f"isalnum(): {word.isalnum()}")
print(f"isspace(): {word.isspace()}")
print(f"istitle(): {word.istitle()}")
print(f"isupper(): {word.isupper()}")
print(f"islower(): {word.islower()}")
print(f"startswith('Py'): {word.startswith('Py')}")
print(f"endswith('3'): {word.endswith('3')}")

# 5. SPLIT AND JOIN
print("\n--- Split and Join ---")
sentence = "Python is a powerful language"
print(f"String: '{sentence}'")
words = sentence.split()
print(f"split(): {words}")
print(f"split('a'): {sentence.split('a')}")

fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")
print(f"'-'.join(fruits): '{'-'.join(fruits)}'")
print(f"', '.join(fruits): '{', '.join(fruits)}'")

# 6. OTHER USEFUL METHODS
print("\n--- Other Methods ---")
text2 = "hello"
print(f"String: '{text2}'")
print(f"center(20, '*'): '{text2.center(20, '*')}'")
print(f"ljust(20, '-'): '{text2.ljust(20, '-')}'")
print(f"rjust(20, '-'): '{text2.rjust(20, '-')}'")
print(f"zfill(10): '{text2.zfill(10)}'")

# ============================================
# STRING FORMATTING
# ============================================
print("\n" + "=" * 50)
print("STRING FORMATTING")
print("=" * 50)

# User details for formatting examples
name = "Dushyant"
age = 20
marks = 85.5678
city = "Delhi"

# 1. USING .format() METHOD
print("\n--- Using .format() Method ---")

# Basic positional formatting
print("Hello, my name is {} and I am {} years old.".format(name, age))

# Using index positions
print("Name: {0}, Age: {1}, City: {2}".format(name, age, city))
print("Repeated: {0} {0} {0}".format(name))

# Using keyword arguments
print("Student: {n}, Marks: {m}".format(n=name, m=marks))

# Formatting numbers
print("Marks (2 decimal): {:.2f}".format(marks))
print("Marks (no decimal): {:.0f}".format(marks))
print("Percentage: {:.1f}%".format(marks))

# Padding and alignment
print("Left aligned: |{:<15}|".format(name))
print("Right aligned: |{:>15}|".format(name))
print("Center aligned: |{:^15}|".format(name))
print("With fill char: |{:*^15}|".format(name))

# Number formatting
num = 1234567
print("With commas: {:,}".format(num))
print("Binary: {:b}".format(42))
print("Hexadecimal: {:x}".format(255))
print("Octal: {:o}".format(64))

# 2. USING F-STRING (f"") - Python 3.6+
print("\n--- Using f-string (Recommended) ---")

# Basic f-string
print(f"Hello, my name is {name} and I am {age} years old.")

# Expressions inside f-string
print(f"Next year I will be {age + 1} years old.")
print(f"Name in uppercase: {name.upper()}")
print(f"Name length: {len(name)} characters")

# Formatting numbers with f-string
print(f"Marks (2 decimal): {marks:.2f}")
print(f"Marks (no decimal): {marks:.0f}")
print(f"Percentage: {marks:.1f}%")

# Padding and alignment with f-string
print(f"Left aligned: |{name:<15}|")
print(f"Right aligned: |{name:>15}|")
print(f"Center aligned: |{name:^15}|")
print(f"With fill char: |{name:*^15}|")

# Number formatting with f-string
print(f"With commas: {num:,}")
print(f"Binary of 42: {42:b}")
print(f"Hex of 255: {255:x}")
print(f"Octal of 64: {64:o}")

# Multi-line f-string
print(f"""
Student Details:
----------------
Name: {name}
Age: {age}
City: {city}
Marks: {marks:.2f}%
""")

# Dictionary with f-string
student = {"name": "Rahul", "score": 92}
print(f"Student {student['name']} scored {student['score']}%")

# Date formatting with f-string
from datetime import datetime
now = datetime.now()
print(f"Current date: {now:%d-%m-%Y}")
print(f"Current time: {now:%H:%M:%S}")
print(f"Full datetime: {now:%d %B %Y, %I:%M %p}")

print("\n" + "=" * 50)
print("END OF STRING GUIDE")
print("=" * 50)
