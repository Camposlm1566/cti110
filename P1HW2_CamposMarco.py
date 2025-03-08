# Marco Campos
# March 2, 2025
# P1HW2
# Creating a program with a simple budget

# Pseudocode:
# 1. Start
# 2. Ask the user to enter their budget
# 3. Ask the user to enter their travel destination
# 4. Ask the user for the amount they will spend on gas
# 5. Ask the user for the amount they will spend on accommodation
# 6. Ask the user for the amount they will spend on food
# 7. Calculate total expenses by adding gas, accommodation, and food expenses
# 8. Subtract total expenses from the budget to get the remaining budget
# 9. Display the travel destination, total expenses, and remaining budget
# 10. End

# Ask the user to enter their budget
budget = float(input("Enter your budget: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: "))

# Ask user for amount they will spend on accommodation
accomodation_expense = float(input("Enter the amount you will spend on  accomodation: "))

# Ask user for amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: "))

# Add Expenses
total_expenses = gas_expense + accomodation_expense + food_expense

#Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print(f"\nTravel Destination: {destination}")
print(f"Total Expenses: ${total_expenses: .2f}")
print(f"Remaining Budget: ${remaining_budget: .2f}")





