#Marco Campos
#March 22, 2025
#P3Lab
#Enter money float

# Get value from user
change = float(input("Enter an amount of money: $"))

# If input is exactly 0.00, return "No Change"
if change == 0.00:
    print("No Change")
else:
    print(f"Change Amount: ${change:.2f}")

    # Convert dollars to cents (avoid floating-point issues)
    change = round(change * 100)

    # Determine how many coins are needed
    num_dollars = change // 100
    change %= 100

    num_quarters = change // 25
    change %= 25

    num_dimes = change // 10
    change %= 10

    num_nickels = change // 5
    change %= 5

    num_pennies = change

    # Print out each denomination if needed
    if num_dollars > 0:
        print(f"{num_dollars} Dollar" if num_dollars == 1 else f"{num_dollars} Dollars")

    if num_quarters > 0:
        print(f"{num_quarters} Quarter" if num_quarters == 1 else f"{num_quarters} Quarters")

    if num_dimes > 0:
        print(f"{num_dimes} Dime" if num_dimes == 1 else f"{num_dimes} Dimes")

    if num_nickels > 0:
        print(f"{num_nickels} Nickel" if num_nickels == 1 else f"{num_nickels} Nickels")

    if num_pennies > 0:
        print(f"{num_pennies} Penny" if num_pennies == 1 else f"{num_pennies} Pennies")
