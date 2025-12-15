# ============================================
# ALL PYTHON LOOPS - Complete Guide
# ============================================

# 1. FOR LOOP
# ============================================
print("=" * 50)
print("1. FOR LOOP")
print("=" * 50)

# Basic for loop with range
print("\n--- For loop with range() ---")
for i in range(5):
    print(f"i = {i}")

# For loop with start, stop, step
print("\n--- For loop with range(start, stop, step) ---")
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(f"i = {i}")

# For loop with negative step (counting down)
print("\n--- Counting down ---")
for i in range(5, 0, -1):
    print(f"Countdown: {i}")
print("Blast off!")

# For loop over a list
print("\n--- For loop over a list ---")
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop over a string
print("\n--- For loop over a string ---")
word = "Python"
for char in word:
    print(f"Character: {char}")

# For loop with index using enumerate()
print("\n--- For loop with enumerate() ---")
colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# For loop with enumerate() starting from custom index
print("\n--- enumerate() with custom start ---")
for index, color in enumerate(colors, start=1):
    print(f"Color {index}: {color}")

# For loop over dictionary
print("\n--- For loop over dictionary ---")
student = {"name": "John", "age": 20, "grade": "A"}

print("Keys:")
for key in student:
    print(f"  {key}")

print("\nValues:")
for value in student.values():
    print(f"  {value}")

print("\nKey-Value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# For loop with zip() - iterate multiple lists
print("\n--- For loop with zip() ---")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# Nested for loops
print("\n--- Nested for loops ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end="  ")
    print()  # New line after each row

# Multiplication table using nested loops
print("\n--- Multiplication Table (1-5) ---")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()


# 2. WHILE LOOP
# ============================================
print("\n" + "=" * 50)
print("2. WHILE LOOP")
print("=" * 50)

# Basic while loop
print("\n--- Basic while loop ---")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with condition
print("\n--- While loop countdown ---")
num = 5
while num > 0:
    print(f"T-minus {num}")
    num -= 1
print("Launch!")

# While loop with user input simulation
print("\n--- While loop with condition check ---")
total = 0
numbers = [10, 20, 30, 0, 40, 50]  # 0 will stop the loop
index = 0
while index < len(numbers) and numbers[index] != 0:
    total += numbers[index]
    print(f"Added {numbers[index]}, Total: {total}")
    index += 1
print(f"Final Total: {total}")

# Infinite loop (controlled)
print("\n--- Controlled infinite loop ---")
counter = 0
while True:
    print(f"Loop iteration: {counter}")
    counter += 1
    if counter >= 3:
        print("Breaking out of infinite loop!")
        break


# 3. BREAK STATEMENT
# ============================================
print("\n" + "=" * 50)
print("3. BREAK STATEMENT")
print("=" * 50)

# Break in for loop
print("\n--- Break in for loop ---")
for i in range(10):
    if i == 5:
        print(f"Found 5! Breaking out of loop.")
        break
    print(f"i = {i}")

# Break in while loop
print("\n--- Break in while loop ---")
num = 0
while num < 100:
    if num == 7:
        print(f"Found 7! Breaking out.")
        break
    print(f"num = {num}")
    num += 1

# Break with search
print("\n--- Using break for searching ---")
numbers = [4, 7, 2, 9, 5, 1, 8, 3]
target = 9
found = False

for num in numbers:
    print(f"Checking {num}...")
    if num == target:
        found = True
        print(f"Found {target}!")
        break

if not found:
    print(f"{target} not found in list")

# Break in nested loops (only breaks inner loop)
print("\n--- Break in nested loops ---")
for i in range(3):
    print(f"Outer loop i = {i}")
    for j in range(5):
        if j == 3:
            print(f"  Breaking inner loop at j = {j}")
            break
        print(f"  Inner loop j = {j}")


# 4. CONTINUE STATEMENT
# ============================================
print("\n" + "=" * 50)
print("4. CONTINUE STATEMENT")
print("=" * 50)

# Continue in for loop - skip even numbers
print("\n--- Continue: Skip even numbers ---")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

# Continue in while loop
print("\n--- Continue in while loop ---")
num = 0
while num < 10:
    num += 1
    if num % 3 == 0:
        print(f"Skipping {num} (divisible by 3)")
        continue
    print(f"Processing: {num}")

# Continue to skip specific items
print("\n--- Continue: Skip specific items ---")
fruits = ["apple", "banana", "cherry", "durian", "elderberry"]
skip_fruits = ["banana", "durian"]

for fruit in fruits:
    if fruit in skip_fruits:
        print(f"Skipping {fruit}...")
        continue
    print(f"I'll eat {fruit}")


# 5. ELSE CLAUSE WITH LOOPS
# ============================================
print("\n" + "=" * 50)
print("5. ELSE CLAUSE WITH LOOPS")
print("=" * 50)

# For-else (else runs if loop completes without break)
print("\n--- For-else: Loop completed ---")
for i in range(5):
    print(f"i = {i}")
else:
    print("Loop completed successfully!")

# For-else with break (else doesn't run)
print("\n--- For-else with break ---")
for i in range(5):
    if i == 3:
        print("Breaking at i = 3")
        break
    print(f"i = {i}")
else:
    print("This won't print because we used break")

# Practical example: Prime number check
print("\n--- Prime number check using for-else ---")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 17
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        print(f"{number} is NOT a prime number (divisible by {i})")
        break
else:
    print(f"{number} IS a prime number!")

# While-else
print("\n--- While-else ---")
count = 0
while count < 3:
    print(f"count = {count}")
    count += 1
else:
    print("While loop finished!")


# 6. PASS STATEMENT
# ============================================
print("\n" + "=" * 50)
print("6. PASS STATEMENT")
print("=" * 50)

# Pass as placeholder
print("\n--- Pass as placeholder ---")
for i in range(5):
    if i == 2:
        pass  # TODO: Add logic later
    else:
        print(f"i = {i}")

# Pass in empty loop (structure placeholder)
print("\n--- Empty loop with pass ---")
for i in range(3):
    pass  # Loop does nothing but is syntactically valid
print("Empty loop completed!")


# 7. LIST COMPREHENSION (Loop shorthand)
# ============================================
print("\n" + "=" * 50)
print("7. LIST COMPREHENSION")
print("=" * 50)

# Basic list comprehension
print("\n--- Basic list comprehension ---")
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# List comprehension with condition
print("\n--- List comprehension with condition ---")
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# List comprehension with if-else
print("\n--- List comprehension with if-else ---")
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(f"Labels: {labels}")

# Nested list comprehension
print("\n--- Nested list comprehension ---")
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:")
for row in matrix:
    print(f"  {row}")


# 8. DICTIONARY & SET COMPREHENSION
# ============================================
print("\n" + "=" * 50)
print("8. DICTIONARY & SET COMPREHENSION")
print("=" * 50)

# Dictionary comprehension
print("\n--- Dictionary comprehension ---")
square_dict = {x: x**2 for x in range(1, 6)}
print(f"Square dict: {square_dict}")

# Set comprehension
print("\n--- Set comprehension ---")
unique_squares = {x**2 for x in [-3, -2, -1, 0, 1, 2, 3]}
print(f"Unique squares: {unique_squares}")


# 9. GENERATOR EXPRESSION (Memory efficient)
# ============================================
print("\n" + "=" * 50)
print("9. GENERATOR EXPRESSION")
print("=" * 50)

# Generator expression
print("\n--- Generator expression ---")
gen = (x**2 for x in range(5))
print(f"Generator object: {gen}")
print("Values from generator:")
for val in gen:
    print(f"  {val}")


# 10. PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 50)
print("10. PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Sum of digits
print("\n--- Sum of digits ---")
number = 12345
digit_sum = 0
temp = number
while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10
print(f"Sum of digits of {number}: {digit_sum}")

# Example 2: Reverse a string
print("\n--- Reverse a string ---")
original = "Python"
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print(f"Original: {original}")
print(f"Reversed: {reversed_str}")

# Example 3: Fibonacci sequence
print("\n--- Fibonacci sequence ---")
n_terms = 10
a, b = 0, 1
print(f"Fibonacci ({n_terms} terms):", end=" ")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
print()

# Example 4: Pattern printing
print("\n--- Pattern: Right triangle ---")
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

print("\n--- Pattern: Pyramid ---")
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars)

print("\n" + "=" * 50)
print("END OF PYTHON LOOPS GUIDE")
print("=" * 50)
