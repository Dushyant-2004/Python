# Encapsulation in Python

"""
DEFINITION:
Encapsulation is one of the fundamental concepts of Object-Oriented Programming (OOP).
It refers to bundling data (attributes) and methods (functions) that operate on the data 
into a single unit called a class, while restricting direct access to some of the object's 
components. This is achieved using access modifiers:

- Public: Accessible from anywhere (no underscore prefix)
- Protected: Accessible within class and subclasses (single underscore _)
- Private: Accessible only within the class (double underscore __)

Encapsulation helps in:
1. Data Hiding - Protecting data from unauthorized access
2. Data Validation - Controlling how data is modified
3. Flexibility - Internal implementation can change without affecting external code
"""

# Example: Bank Account with Encapsulation

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder      # Public attribute
        self.__balance = initial_balance          # Private attribute (encapsulated)
    
    # Getter method - to access private attribute
    def get_balance(self):
        return self.__balance
    
    # Setter method - to modify private attribute with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Invalid withdrawal amount or insufficient funds!")
    
    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.__balance}")


# Creating an object
account = BankAccount("Dushyant", 1000)

print("=== Encapsulation Example: Bank Account ===\n")

# Accessing public attribute (allowed)
print(f"Account Holder: {account.account_holder}")

# Accessing private attribute directly (will cause error)
# print(account.__balance)  # This will raise AttributeError

# Accessing private attribute through getter method (correct way)
print(f"Balance: ${account.get_balance()}")

print()

# Modifying balance through methods (encapsulated way)
account.deposit(500)
account.withdraw(200)

print()
account.display_info()
