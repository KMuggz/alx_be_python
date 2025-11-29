# this script 'bank_account.py' houses banking operations

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with a starting balance (default 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the amount if funds are sufficient.
        Returns True if successful, False otherwise.
        """
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")