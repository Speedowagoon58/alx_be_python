class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance  # Use instance attribute and initial_balance

    def deposit(self, amount):
        self.account_balance += amount  # Update instance attribute

    def withdraw(self, amount):
        if self.account_balance >= amount:  # Check if funds are sufficient
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Your current balance is: ${self.account_balance}.")  # Proper formatting
