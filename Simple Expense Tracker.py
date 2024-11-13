expenses = {}

def add_expense(date, amount, description):
    expenses[date] = {"amount": amount, "description": description}
    print("Expense added successfully")

def view_expenses():
    for date, expense in expenses.items():
        print(f"{date}: {expense['amount']} - {expense['description']}")

def delete_expense(date):
    if date in expenses:
        del expenses[date]
        print("Expense deleted successfully")
    else:
        print("Expense not found")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        date = input("Enter date: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        add_expense(date, amount, description)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        date = input("Enter date: ")
        delete_expense(date)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
