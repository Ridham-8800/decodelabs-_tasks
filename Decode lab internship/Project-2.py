# Expense Tracker

total = 0  # accumulator variable

n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    expense = float(input(f"Enter expense {i+1}: "))
    total = total + expense

print("\nTotal Spent =", total)