# Marco Campos
# March 29, 2025
#P3HW1
#Debug the orginal file 


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)  # Ensure avg is defined

# Determine letter grade for average
if avg >= 90:
    letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'
elif avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:     {low:.1f}")
print(f"Highest Grade:    {high:.1f}")
print(f"Sum of Grades:    {total:.1f}")
print(f"Average:          {avg:.2f}")
print("--------------------------------")
print(f"Your grade is: {letter_grade}")

