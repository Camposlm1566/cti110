#Marco Campos
#March 16, 2025
#P2HW1
#Adding onto P1HW2 assignment


print("This program calculates and displays travel expenses")

budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"Fuel: {gas}")
print(f"Accommodation: {hotel}")
print(f"Food: {food}")
print(f"\nRemaining Balance: {remaining_balance}")



# Display formatted output
print("\n------------ Travel Expenses ------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${gas:,.2f}")
print(f"{'Accommodation:':<20} ${hotel:,.2f}")
print(f"{'Food:':<20} ${food:,.2f}")
print(f"\n{'Remaining Balance:':<20} ${remaining_balance:,.2f}")
