class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance  # Initialize with starting balance

    def deposit(self, amount):
        self.account_balance += amount  # Add to balance

    def withdraw(self, amount):
        if self.account_balance >= amount:  # Check if enough funds
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")  # Format to two decimal places
