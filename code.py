# ============================================
# ALL PYTHON OPERATORS - Complete Guide
# ============================================

# 1. ARITHMETIC OPERATORS
# ============================================
print("=" * 50)
print("1. ARITHMETIC OPERATORS")
print("=" * 50)

a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")           # 19
print(f"Subtraction (a - b): {a - b}")        # 11
print(f"Multiplication (a * b): {a * b}")     # 60
print(f"Division (a / b): {a / b}")           # 3.75
print(f"Floor Division (a // b): {a // b}")   # 3
print(f"Modulus (a % b): {a % b}")            # 3
print(f"Exponentiation (a ** b): {a ** b}")   # 50625

# 2. COMPARISON (RELATIONAL) OPERATORS
# ============================================
print("\n" + "=" * 50)
print("2. COMPARISON OPERATORS")
print("=" * 50)

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"Equal to (x == y): {x == y}")                 # False
print(f"Not equal to (x != y): {x != y}")             # True
print(f"Greater than (x > y): {x > y}")               # False
print(f"Less than (x < y): {x < y}")                  # True
print(f"Greater than or equal (x >= y): {x >= y}")    # False
print(f"Less than or equal (x <= y): {x <= y}")       # True

# 3. LOGICAL OPERATORS
# ============================================
print("\n" + "=" * 50)
print("3. LOGICAL OPERATORS")
print("=" * 50)

p = True
q = False

print(f"p = {p}, q = {q}")
print(f"Logical AND (p and q): {p and q}")    # False
print(f"Logical OR (p or q): {p or q}")       # True
print(f"Logical NOT (not p): {not p}")        # False
print(f"Logical NOT (not q): {not q}")        # True

# 4. BITWISE OPERATORS
# ============================================
print("\n" + "=" * 50)
print("4. BITWISE OPERATORS")
print("=" * 50)

m = 12  # Binary: 1100
n = 7   # Binary: 0111

print(f"m = {m} (binary: {bin(m)})")
print(f"n = {n} (binary: {bin(n)})")
print(f"Bitwise AND (m & n): {m & n} (binary: {bin(m & n)})")       # 4
print(f"Bitwise OR (m | n): {m | n} (binary: {bin(m | n)})")        # 15
print(f"Bitwise XOR (m ^ n): {m ^ n} (binary: {bin(m ^ n)})")       # 11
print(f"Bitwise NOT (~m): {~m} (binary: {bin(~m)})")                # -13
print(f"Left Shift (m << 2): {m << 2} (binary: {bin(m << 2)})")     # 48
print(f"Right Shift (m >> 2): {m >> 2} (binary: {bin(m >> 2)})")    # 3

# 5. ASSIGNMENT OPERATORS
# ============================================
print("\n" + "=" * 50)
print("5. ASSIGNMENT OPERATORS")
print("=" * 50)

num = 10
print(f"Initial value: num = {num}")

num += 5    # num = num + 5
print(f"After num += 5: {num}")     # 15

num -= 3    # num = num - 3
print(f"After num -= 3: {num}")     # 12

num *= 2    # num = num * 2
print(f"After num *= 2: {num}")     # 24

num /= 4    # num = num / 4
print(f"After num /= 4: {num}")     # 6.0

num //= 2   # num = num // 2
print(f"After num //= 2: {num}")    # 3.0

num **= 3   # num = num ** 3
print(f"After num **= 3: {num}")    # 27.0

num %= 5    # num = num % 5
print(f"After num %= 5: {num}")     # 2.0

# Bitwise Assignment Operators
val = 12
print(f"\nBitwise Assignment (val = {val}):")

val &= 7    # val = val & 7
print(f"After val &= 7: {val}")     # 4

val |= 8    # val = val | 8
print(f"After val |= 8: {val}")     # 12

val ^= 3    # val = val ^ 3
print(f"After val ^= 3: {val}")     # 15

val >>= 2   # val = val >> 2
print(f"After val >>= 2: {val}")    # 3

val <<= 3   # val = val << 3
print(f"After val <<= 3: {val}")    # 24

# 6. IDENTITY OPERATORS
# ============================================
print("\n" + "=" * 50)
print("6. IDENTITY OPERATORS")
print("=" * 50)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")

print(f"\nlist1 is list2: {list1 is list2}")           # False (different objects)
print(f"list1 is list3: {list1 is list3}")             # True (same object)
print(f"list1 is not list2: {list1 is not list2}")     # True
print(f"list1 == list2: {list1 == list2}")             # True (same values)

# 7. MEMBERSHIP OPERATORS
# ============================================
print("\n" + "=" * 50)
print("7. MEMBERSHIP OPERATORS")
print("=" * 50)

my_list = [1, 2, 3, 4, 5]
my_string = "Hello World"
my_dict = {"name": "John", "age": 25}

print(f"my_list = {my_list}")
print(f"my_string = '{my_string}'")
print(f"my_dict = {my_dict}")

print(f"\n3 in my_list: {3 in my_list}")               # True
print(f"10 in my_list: {10 in my_list}")               # False
print(f"10 not in my_list: {10 not in my_list}")       # True

print(f"\n'Hello' in my_string: {'Hello' in my_string}")       # True
print(f"'Python' in my_string: {'Python' in my_string}")       # False
print(f"'Python' not in my_string: {'Python' not in my_string}") # True

print(f"\n'name' in my_dict: {'name' in my_dict}")     # True (checks keys)
print(f"'John' in my_dict: {'John' in my_dict}")       # False (not a key)

# 8. WALRUS OPERATOR (:=) - Python 3.8+
# ============================================
print("\n" + "=" * 50)
print("8. WALRUS OPERATOR (:=)")
print("=" * 50)

# Assigns and returns value in same expression
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Without walrus operator
length = len(numbers)
if length > 5:
    print(f"List has {length} elements (without walrus)")

# With walrus operator
if (n := len(numbers)) > 5:
    print(f"List has {n} elements (with walrus)")

# 9. TERNARY (CONDITIONAL) OPERATOR
# ============================================
print("\n" + "=" * 50)
print("9. TERNARY OPERATOR")
print("=" * 50)

age = 18
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

score = 85
grade = "Pass" if score >= 50 else "Fail"
print(f"Score: {score}, Grade: {grade}")

# ============================================
# OPERATOR PRECEDENCE (Highest to Lowest)
# ============================================
print("\n" + "=" * 50)
print("OPERATOR PRECEDENCE (Highest to Lowest)")
print("=" * 50)
print("""
1.  ()              - Parentheses
2.  **              - Exponentiation
3.  +x, -x, ~x      - Unary plus, minus, bitwise NOT
4.  *, /, //, %     - Multiplication, Division, Floor, Modulus
5.  +, -            - Addition, Subtraction
6.  <<, >>          - Bitwise shifts
7.  &               - Bitwise AND
8.  ^               - Bitwise XOR
9.  |               - Bitwise OR
10. ==, !=, <, <=, >, >=, is, is not, in, not in  - Comparisons
11. not             - Logical NOT
12. and             - Logical AND
13. or              - Logical OR
14. :=              - Walrus operator
""")

# Example of precedence
print("Precedence Example:")
result = 2 + 3 * 4 ** 2
print(f"2 + 3 * 4 ** 2 = {result}")  # 2 + 3 * 16 = 2 + 48 = 50

result_with_parens = (2 + 3) * 4 ** 2
print(f"(2 + 3) * 4 ** 2 = {result_with_parens}")  # 5 * 16 = 80

print("\n" + "=" * 50)
print("END OF PYTHON OPERATORS GUIDE")
print("=" * 50)
