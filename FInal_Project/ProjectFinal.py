# List to store incomes and expenses
incomes = []
expenses = []

# 1. Add Income
def add_income(amount: float, description: str):
    """Add an income entry."""
    incomes.append((amount, description))
    print(f"Income of {amount} added: {description}")

# 2. Add Expense
def add_expense(amount: float, description: str):
    """Add an expense entry."""
    expenses.append((amount, description))
    print(f"Expense of {amount} added: {description}")

# 3. View Balance
def view_balance():
    """Calculate and display the current balance."""
    total_income = sum(item[0] for item in incomes)
    total_expense = sum(item[0] for item in expenses)
    balance = total_income - total_expense
    print(f"\nTotal Income: {total_income}, Total Expenses: {total_expense}")
    print(f"Current Balance: {balance}")
    return total_income, total_expense, balance

# 4. Save Data to File (Separate File for Each Session)
def save_to_file(date: str):
    """Save the incomes, expenses, and balance data to a new text file."""
    
    total_income, total_expense, balance = view_balance()  # Get current financial summary
    
    filename = f"data_{date}.txt"  # Create a unique filename with the date
    with open(filename, 'w') as file:  # 'w' mode to create a new file for each session
        file.write(f"Data for {date}:\n")
        file.write("\nIncomes:\n")
        for amount, description in incomes:
            file.write(f"Amount: {amount}, Description: {description}\n")
        
        file.write("\nExpenses:\n")
        for amount, description in expenses:
            file.write(f"Amount: {amount}, Description: {description}\n")
        
        # Write totals and current balance at the end of the file
        file.write(f"\nTotal Income: {total_income}\n")
        file.write(f"Total Expenses: {total_expense}\n")
        file.write(f"Current Balance: {balance}\n")
        file.write("="*30 + "\n")  # Separator for clarity
    
    print(f"Data saved in {filename}")

# 5. Function to Get User Input for Incomes and Expenses
def get_user_input(transaction_type: str):
    """
    Handle user input for incomes or expenses.
    Args:
    transaction_type (str): Should be either 'income' or 'expense' to determine the type of transaction.
    """
    if transaction_type == 'income':
        print("\nEnter incomes for the session. Type 'done' when finished.")
        while True:
            description = input("Enter income description (or type 'done' to finish): ")
            if description.lower() == 'done':
                break
            try:
                amount = float(input(f"Enter amount for '{description}': "))
                add_income(amount, description)
            except ValueError:
                print("Please enter a valid number for the amount.")
    elif transaction_type == 'expense':
        print("\nEnter expenses for the session. Type 'done' when finished.")
        while True:
            description = input("Enter expense description (or type 'done' to finish): ")
            if description.lower() == 'done':
                break
            try:
                amount = float(input(f"Enter amount for '{description}': "))
                add_expense(amount, description)
            except ValueError:
                print("Please enter a valid number for the amount.")
    else:
        print("Invalid transaction type.")

# Main program to interactively input incomes and expenses
if __name__ == "__main__":
    # Ask the user for the date of this session
    session_date = input("Enter the date for this session (YYYY-MM-DD): ")
    
    # Get user inputs for incomes and expenses using the new function
    get_user_input('income')  # For incomes
    get_user_input('expense')  # For expenses
    
    # View summary of incomes and expenses (just to print in console)
    view_balance()
    
    # Save the data to a new file with the session's date in the filename
    save_to_file(session_date)