# ============================================
# FUNCTION EXAMPLES WITH USER INPUT
# ============================================

# EXAMPLE 1: Calculator Function
# ============================================
print("=" * 50)
print("EXAMPLE 1: SIMPLE CALCULATOR")
print("=" * 50)

def calculator(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.
    
    Parameters:
        num1: First number
        num2: Second number
        operation: +, -, *, /
    
    Returns:
        Result of the operation
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operation!"

# Taking input from user
print("\n--- Calculator ---")
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

# Calling the function
result = calculator(first_num, second_num, op)
print(f"\nResult: {first_num} {op} {second_num} = {result}")


# EXAMPLE 2: Student Grade Calculator
# ============================================
print("\n" + "=" * 50)
print("EXAMPLE 2: STUDENT GRADE CALCULATOR")
print("=" * 50)

def calculate_grade(marks):
    """
    Calculates grade based on marks.
    
    Parameters:
        marks: Student's marks (0-100)
    
    Returns:
        Tuple of (grade, remark)
    """
    if marks >= 90:
        return 'A+', 'Excellent!'
    elif marks >= 80:
        return 'A', 'Very Good!'
    elif marks >= 70:
        return 'B', 'Good'
    elif marks >= 60:
        return 'C', 'Average'
    elif marks >= 50:
        return 'D', 'Pass'
    else:
        return 'F', 'Fail'

def get_student_result(name, marks_list):
    """
    Calculates total, percentage and grade for a student.
    
    Parameters:
        name: Student's name
        marks_list: List of marks in different subjects
    
    Returns:
        Dictionary with student results
    """
    total = sum(marks_list)
    percentage = total / len(marks_list)
    grade, remark = calculate_grade(percentage)
    
    return {
        'name': name,
        'total': total,
        'percentage': round(percentage, 2),
        'grade': grade,
        'remark': remark
    }

# Taking input from user
print("\n--- Student Grade Calculator ---")
student_name = input("Enter student name: ")
num_subjects = int(input("Enter number of subjects: "))

marks = []
for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

# Calling the function
student_result = get_student_result(student_name, marks)

# Displaying results
print("\n" + "-" * 30)
print("RESULT CARD")
print("-" * 30)
print(f"Name: {student_result['name']}")
print(f"Total Marks: {student_result['total']}")
print(f"Percentage: {student_result['percentage']}%")
print(f"Grade: {student_result['grade']}")
print(f"Remark: {student_result['remark']}")
print("-" * 30)
