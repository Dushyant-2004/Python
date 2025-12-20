# Abstraction in Python

"""
DEFINITION:
Abstraction is a fundamental concept of Object-Oriented Programming (OOP) that focuses 
on hiding the complex implementation details and showing only the essential features 
of an object. It helps in reducing complexity and isolating the impact of changes.

In Python, abstraction is achieved using:
1. Abstract Classes - Classes that cannot be instantiated and may contain abstract methods
2. Abstract Methods - Methods declared but contain no implementation (must be overridden)

Key Points:
- We use the 'abc' module (Abstract Base Class) to create abstract classes
- Abstract classes can have both abstract methods and concrete methods
- Child classes MUST implement all abstract methods of the parent class
- Abstract classes cannot be instantiated directly

Real-world Analogy:
When you drive a car, you only interact with steering wheel, pedals, and gear.
You don't need to know how the engine works internally - that complexity is abstracted away.
"""

from abc import ABC, abstractmethod

# Example: Payment System using Abstraction

# Abstract Class (Base Class)
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount
    
    # Abstract method - MUST be implemented by child classes
    @abstractmethod
    def process_payment(self):
        pass
    
    # Abstract method
    @abstractmethod
    def get_payment_details(self):
        pass
    
    # Concrete method - can be used by all child classes
    def display_amount(self):
        print(f"Payment Amount: ${self.amount}")


# Concrete Class 1 - Implements all abstract methods
class CreditCardPayment(Payment):
    def __init__(self, amount, card_number, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.cvv = cvv
    
    # Implementing abstract method
    def process_payment(self):
        print(f"Processing credit card payment of ${self.amount}")
        print("Connecting to bank server...")
        print("Payment successful via Credit Card!")
    
    # Implementing abstract method
    def get_payment_details(self):
        # Hiding full card number for security (showing last 4 digits)
        masked_card = "**** **** **** " + self.card_number[-4:]
        print(f"Card Number: {masked_card}")
        print(f"Amount: ${self.amount}")


# Concrete Class 2 - Implements all abstract methods
class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id
    
    # Implementing abstract method
    def process_payment(self):
        print(f"Processing UPI payment of ${self.amount}")
        print(f"Sending request to {self.upi_id}...")
        print("Payment successful via UPI!")
    
    # Implementing abstract method
    def get_payment_details(self):
        print(f"UPI ID: {self.upi_id}")
        print(f"Amount: ${self.amount}")


# Concrete Class 3 - Implements all abstract methods
class NetBankingPayment(Payment):
    def __init__(self, amount, bank_name, account_number):
        super().__init__(amount)
        self.bank_name = bank_name
        self.account_number = account_number
    
    # Implementing abstract method
    def process_payment(self):
        print(f"Processing Net Banking payment of ${self.amount}")
        print(f"Redirecting to {self.bank_name} portal...")
        print("Payment successful via Net Banking!")
    
    # Implementing abstract method
    def get_payment_details(self):
        masked_account = "XXXXXX" + self.account_number[-4:]
        print(f"Bank: {self.bank_name}")
        print(f"Account: {masked_account}")
        print(f"Amount: ${self.amount}")


# Main Program
print("=== Abstraction Example: Payment System ===\n")

# This will cause error - Cannot instantiate abstract class
# payment = Payment(100)  # TypeError: Can't instantiate abstract class

# Creating objects of concrete classes
print("--- Credit Card Payment ---")
cc_payment = CreditCardPayment(1500, "1234567890123456", "123")
cc_payment.get_payment_details()
cc_payment.display_amount()  # Using concrete method from parent
cc_payment.process_payment()

print("\n--- UPI Payment ---")
upi_payment = UPIPayment(500, "dushyant@upi")
upi_payment.get_payment_details()
upi_payment.process_payment()

print("\n--- Net Banking Payment ---")
nb_payment = NetBankingPayment(2000, "SBI Bank", "9876543210")
nb_payment.get_payment_details()
nb_payment.process_payment()
