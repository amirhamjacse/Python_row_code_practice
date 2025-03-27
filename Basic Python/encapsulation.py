# Define a class with private attributes (encapsulation)
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute (encapsulated)

    # Getter for the balance (to access the private attribute)
    def get_balance(self):
        return self.__balance

    # Setter to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount!")

# Create an object of the BankAccount class
account = BankAccount("Alice", 1000)

# Access the public method to deposit money
account.deposit(500)  # Output: Deposited 500. New balance: 1500

# Access the balance using getter
print(account.get_balance())  # Output: 1500
