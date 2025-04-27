#Marco Campos
#April 12, 2025
#P4HW2
#Create a program that allows user to enter employees information

# ---------------------------------------------
# Pseudocode:
# - Loop to ask for employee name until user types "Done"
# - For each employee:
#   - Ask for hours worked and pay rate
#   - Calculate regular hours, overtime hours, and pay
#   - Display employee pay breakdown
#   - Add to running totals
# - After "Done", display:
#   - Total employees entered
#   - Total overtime pay
#   - Total regular pay
#   - Total gross pay
# ---------------------------------------------


# Initialize totals
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

while True:
    name = input('Enter employee\'s name or "Done" to terminate: ').strip()

    if name.lower() == "done":
        break  # Exit the loop if user is finished

    try:
        # Get hours worked and pay rate
        hours_worked = float(input(f"How many hours did {name} work? "))
        pay_rate = float(input(f"What is {name}'s pay rate? "))

        # Calculate regular and overtime hours
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            regular_hours = 40
        else:
            overtime_hours = 0
            regular_hours = hours_worked

        # Pay calculations
        regular_pay = regular_hours * pay_rate
        overtime_pay = overtime_hours * pay_rate * 1.5
        gross_pay = regular_pay + overtime_pay

        # Display the employee's pay breakdown
        print(f"\nEmployee name:  {name}")
        print("\nHours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay")
        print("--------------------------------------------------------------------------")
        print(f"{hours_worked:<13.1f}{pay_rate:<9.2f}{overtime_hours:<10.1f}"
              f"${overtime_pay:<13.2f}${regular_pay:<12.2f}${gross_pay:.2f}\n")

        # Update totals
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        employee_count += 1

    except ValueError:
        print("⚠️ Invalid input. Please enter numbers for hours and pay rate.\n")

# Display overall summary
print("\n----------------------------------------")
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime:     ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross:          ${total_gross_pay:.2f}")
print("----------------------------------------")



