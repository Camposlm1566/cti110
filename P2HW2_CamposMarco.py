#Marco Campos
#March 16, 2025
#P2HW2
#Design program that allows user to enter grades

"""
Pseudocode:
1. Display a message asking the user to enter grades for six modules.
2. Create an empty list to store the grades.
3. Use input statements to collect six grades from the user.
4. Convert each input to a float and append it to the list.
5. Calculate the following:
   - Lowest grade using min()
   - Highest grade using max()
   - Sum of all grades using sum()
   - Average by dividing the sum by the number of grades
6. Display the results in the required format with proper spacing and rounding.
"""

# Step 1: Create an empty list to store grades
grades = []

# Step 2: Prompt the user to enter grades for each module
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# Step 3: Perform calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Step 4: Display the results in the required format
print("\n------------Results------------")
print(f"Lowest Grade:     {lowest}")
print(f"Highest Grade:    {highest}")
print(f"Sum of Grades:    {total}")
print(f"Average:          {average:.2f}")  # Displaying average with two decimal places
