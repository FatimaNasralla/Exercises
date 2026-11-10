#  Project 1 – Expense Tracker CLI App
# | A full program combining file I/O, classes, user input, conditionals, lists, and dictionaries. 📌 Objective:

# Create a command-line expense tracker where users can:

# Add a new expense (category, amount, date)
# View all expenses
# View total spent per category
# Save & load expenses from a CSV file
# 🧩 Features:

# Expense class: holds category, amount, date
# ExpenseManager class:
# .add_expense()
# .view_expenses()
# .category_summary()
# .save_to_csv() and .load_from_csv()
# | Note: You can skip the hard section until you finish the Machine Learning Practice Course, Because it includes the libraries that you want to work with in order to read and write csv, such as Pandas
import csv

class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"{self.date}: {self.category} - ${self.amount:.2f}"


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def view_expenses(self):
        for expense in self.expenses:
            print(expense)

    def category_summary(self):
        summary = {}
        for expense in self.expenses:
            if expense.category in summary:
                summary[expense.category] += expense.amount
            else:
                summary[expense.category] = expense.amount
        for category, total in summary.items():
            print(f"{category}: ${total}")

    def save_to_csv(self):
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["category", "amount", "date"])

            for expense in self.expenses:
                writer.writerow([
                    expense.category,
                    expense.amount,
                    expense.date
             ])

    def load_from_csv(self):
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                category = row[0]
                amount = float(row[1])
                date = row[2]

                expense = Expense(category, amount, date)

                self.expenses.append(expense)


expense1 = Expense("Food", 15, "2026-11-10")
expense2 = Expense("Transport", 10, "2026-11-10")

manager = ExpenseManager()

manager.expenses.append(expense1)
manager.expenses.append(expense2)

manager.view_expenses()
manager.category_summary()

# manager = ExpenseManager()

# manager.add_expense("Food", 15, "2026-11-10")
# manager.add_expense("Transport", 10, "2026-11-10")

# manager.save_to_csv()

# manager2 = ExpenseManager()

# manager2.load_from_csv()

# manager2.view_expenses()