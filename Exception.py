# Exception Handling in Python
# Using try, except, else, and finally keywords

"""
Exception Handling Keywords:
- try     : Contains code that might raise an exception
- except  : Handles the exception if one occurs
- else    : Executes if NO exception occurs in try block
- finally : ALWAYS executes, whether exception occurred or not
"""

# Example: Division Calculator with Complete Exception Handling

def divide_numbers(a, b):
    """Function to demonstrate exception handling"""
    try:
        # Code that might raise an exception
        result = a / b
        
    except ZeroDivisionError:
        # Handles division by zero error
        print("❌ Error: Cannot divide by zero!")
        return None
        
    except TypeError:
        # Handles wrong data type error
        print("❌ Error: Please provide numbers only!")
        return None
        
    else:
        # Executes only if NO exception occurred
        print(f"✅ Division successful!")
        print(f"   {a} / {b} = {result}")
        return result
        
    finally:
        # ALWAYS executes (cleanup code)
        print("🔄 Operation completed. (finally block executed)\n")


# Testing the function with different scenarios
print("=" * 50)
print("EXCEPTION HANDLING DEMONSTRATION")
print("=" * 50)

# Test 1: Normal division (no exception)
print("\n📌 Test 1: Normal Division (10 / 2)")
divide_numbers(10, 2)

# Test 2: Division by zero (ZeroDivisionError)
print("📌 Test 2: Division by Zero (10 / 0)")
divide_numbers(10, 0)

# Test 3: Wrong data type (TypeError)
print("📌 Test 3: Wrong Data Type (10 / 'a')")
divide_numbers(10, "a")

"""
OUTPUT EXPLANATION:
-------------------
Test 1: try → else → finally (No exception)
Test 2: try → except → finally (ZeroDivisionError caught)
Test 3: try → except → finally (TypeError caught)

KEY POINTS:
- 'else' runs ONLY when try block succeeds
- 'finally' ALWAYS runs (useful for cleanup like closing files)
"""
