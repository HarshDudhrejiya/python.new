# Python Mini Project: Personal Expense Tracker
# Features: add expenses, list, summary by category, export to CSV

import csv
from datetime import datetime

EXPENSES = []


def add_expense():
    name = input("Item name: ").strip()
    category = input("Category (food, travel, bills, other): ").strip().lower()
    amount = float(input("Amount: "))
    date_str = input("Date (YYYY-MM-DD) [today]: ").strip()
    date = datetime.today().date() if not date_str else datetime.strptime(date_str, "%Y-%m-%d").date()
    EXPENSES.append({"name": name, "category": category, "amount": amount, "date": str(date)})
    print("Added!\n")


def list_expenses():
    if not EXPENSES:
        print("No expenses yet.\n")
        return
    for i, e in enumerate(EXPENSES, start=1):
        print(f"{i}. {e['date']} - {e['name']} - {e['category']} - ${e['amount']:.2f}")
    print()


def summary_by_category():
    totals = {}
    for e in EXPENSES:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    if not totals:
        print("No expenses to summarize.\n")
        return
    for cat, total in totals.items():
        print(f"{cat.title()}: ${total:.2f}")
    print()


def export_csv():
    if not EXPENSES:
        print("No data to export.\n")
        return
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "name", "category", "amount"])
        writer.writeheader()
        writer.writerows(EXPENSES)
    print("Exported to expenses.csv\n")


def main():
    while True:
        print("1) Add Expense")
        print("2) List Expenses")
        print("3) Summary by Category")
        print("4) Export to CSV")
        print("5) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            export_csv()
        elif choice == "5":
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
