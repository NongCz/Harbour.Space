import os
from datetime import datetime

# Session 8: Decorators
def transaction_logger(func):
    """Decorator to log transaction details after income/expense is added."""
    def wrapper(self, amount, description):
        result = func(self, amount, description)
        print(f"Logged: {description} of {amount}")
        return result
    return wrapper

# Session 3 and 4: OOP with Class 1 and 2
class FinanceTracker:
    def __init__(self):
        # Session 1: Using Lists to Store Incomes and Expenses
        self.incomes = []
        self.expenses = []

    @transaction_logger
    def add_income(self, amount: float, description: str):
        """Add an income entry."""
        self.incomes.append((amount, description))
        print(f"Income of {amount} added: {description}")

    @transaction_logger
    def add_expense(self, amount: float, description: str):
        """Add an expense entry."""
        self.expenses.append((amount, description))
        print(f"Expense of {amount} added: {description}")

    def view_balance(self):
        """Calculate and display the current balance."""
        total_income = sum(item[0] for item in self.incomes)
        total_expense = sum(item[0] for item in self.expenses)
        balance = total_income - total_expense
        print(f"\nTotal Income: {total_income:.2f}, Total Expenses: {total_expense:.2f}")
        print(f"Current Balance: {balance:.2f}")
        return total_income, total_expense, balance

    # Session 7: Using Context Manager for File Operations
    def save_to_file(self, date: str):
        """Save data to a file with session's date in the filename."""
        total_income, total_expense, balance = self.view_balance()

        filename = os.path.join("data", f"data_{date}.txt")
        os.makedirs("data", exist_ok=True)  # Create data folder if it doesn't exist

        # Session 6: Strings and Encodings with 'utf-8' encoding
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"Data for {date}:\n")
            file.write("\nIncomes:\n")
            for amount, description in self.incomes:
                file.write(f"Amount: {amount}, Description: {description}\n")
            file.write("\nExpenses:\n")
            for amount, description in self.expenses:
                file.write(f"Amount: {amount}, Description: {description}\n")
            file.write(f"\nTotal Income: {total_income:.2f}\n")
            file.write(f"Total Expenses: {total_expense:.2f}\n")
            file.write(f"Current Balance: {balance:.2f}\n")
            file.write("="*30 + "\n")
        print(f"Data saved in {filename}")

    def read_existing_data(self, date: str):
        """Check if a file exists and display the data if it exists."""
        filename = os.path.join("data", f"data_{date}.txt")
        if os.path.exists(filename):
            print(f"\nData for {date} exists. Displaying previous data:\n")
            with open(filename, 'r', encoding='utf-8') as file:
                print(file.read())
        else:
            print(f"No existing data for {date}. Proceeding with new entry.")

    # Session 2: Error Handling for User Inputs
    def get_user_input(self, transaction_type: str):
        """
        Get input for incomes or expenses.
        Args:
        transaction_type (str): 'income' or 'expense' to determine type.
        """
        if transaction_type not in ['income', 'expense']:
            print("Invalid transaction type.")
            return

        print(f"\nEnter {transaction_type}s for the session. Type 'done' to finish.")
        while True:
            description = input(f"Enter {transaction_type} description (or type 'done' to finish): ")
            if description.lower() == 'done':
                break
            try:
                amount = float(input(f"Enter amount for '{description}': "))
                if transaction_type == 'income':
                    self.add_income(amount, description)
                else:
                    self.add_expense(amount, description)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

def get_session_date():
    """Prompt user for a date with error handling for correct format."""
    while True:
        date_str = input("Enter the date for this session (YYYY-MM-DD): ")
        try:
            # Session 2: Error Handling for Date Format
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")

# Main program to interactively input incomes and expenses
if __name__ == "__main__":
    # Initialize finance tracker instance
    finance_tracker = FinanceTracker()

    # Get and validate session date
    session_date = get_session_date()

    # Read any existing data for the date
    finance_tracker.read_existing_data(session_date)

    # Input incomes and expenses
    finance_tracker.get_user_input('income')
    finance_tracker.get_user_input('expense')

    # Show balance summary
    finance_tracker.view_balance()

    # Save data to a file
    finance_tracker.save_to_file(session_date)
