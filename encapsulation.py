class Person:
    def __init__(self, name, age):
        # Public attribute
        self.name = name
        # Private attribute
        self.__age = age

    # Public method (getter)
    def get_age(self):
        return self.__age

    # Public method (setter)
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be a positive number.")

    # Method to display the person's details
    def display(self):
        print(f"Name: {self.name}, Age: {self.get_age()}")

# Creating an instance of Person
person = Person("John", 30)

# Accessing public attribute directly
print(person.name)  # Output: John

# Trying to access private attribute directly (will cause error)
# print(person.__age)  # This will raise an AttributeError

# Accessing private attribute via getter
print(person.get_age())  # Output: 30

# Changing private attribute using setter
person.set_age(35)
print(person.get_age())  # Output: 35

# Trying to set an invalid age
person.set_age(-5)  # Output: Age must be a positive number.



#Example: Real-World Use Case (Bank Account)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

# Create a BankAccount object
account = BankAccount(1000)

# Access balance via getter method
print("Balance:", account.get_balance())  # Output: 1000

# Deposit money
account.deposit(500)
print("Balance after deposit:", account.get_balance())  # Output: 1500

# Try to withdraw more than available balance
account.withdraw(2000)  # Output: Insufficient balance or invalid withdrawal amount.

# Withdraw valid amount
account.withdraw(400)
print("Balance after withdrawal:", account.get_balance())  # Output: 1100



