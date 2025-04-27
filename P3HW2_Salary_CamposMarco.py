#Marco Campos
#March 29, 2025
#P3HW2
#Create a program that allows user to enter employees information
# Pseudocode:
# 1. Ask user to enter employee's name.
# 2. Ask user to enter number of hours worked.
# 3. Ask user to enter employee's pay rate.
# 4. Check if hours worked > 40:
#    a. If true, calculate overtime hours (hours_worked - 40).
#    b. Calculate overtime pay (overtime_hours * pay_rate * 1.5).
#    c. Calculate regular pay (40 * pay_rate).
# 5. If hours worked <= 40:
#    a. No overtime, so overtime hours = 0 and overtime pay = 0.
#    b. Regular pay = hours_worked * pay_rate.
# 6. Calculate gross pay (regular pay + overtime pay).
# 7. Display employee details (name, hours worked, pay rate, overtime hours, overtime pay, regular pay, gross pay).

# Get input from user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Initialize variables
overtime_hours = 0
overtime_pay = 0
regular_pay = 0

# Check if employee worked overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40  # Calculate overtime hours
    overtime_pay = overtime_hours * pay_rate * 1.5  # Overtime pay at 1.5x rate
    regular_pay = 40 * pay_rate  # Regular pay for first 40 hours
else:
    regular_pay = hours_worked * pay_rate  # No overtime, all hours are regular

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("\n-------------------------------------------")
print(f"Employee name:   {employee_name}")
print("\nHours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("-----------------------------------------------------------------------------")
print(f"{hours_worked:<14.1f} {pay_rate:<10.2f} {overtime_hours:<10.1f} ${overtime_pay:<14.2f} ${regular_pay:<14.2f} ${gross_pay:<10.2f}")
