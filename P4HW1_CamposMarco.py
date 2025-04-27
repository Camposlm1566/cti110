#Marco Campos
#April 12,2025
#P4HW1
#Creating a loop to collect number of scores


# ---------------------------------------------
# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store valid scores.
# 3. Loop through the number of scores:
#    a. Ask for a score.
#    b. If score is not between 0 and 100:
#       - Show an INVALID message.
#       - Keep asking until a valid score is entered.
#    c. Add the valid score to the score list.
# 4. After collecting all scores:
#    a. Find and display the lowest score.
#    b. Create a new list without the lowest score.
#    c. Calculate the average of the new list.
#    d. Determine the letter grade from the average:
#       - A: 90–100
#       - B: 80–89
#       - C: 70–79
#       - D: 60–69
#       - F: below 60
#    e. Display results: lowest score, new list, average, grade.
# ---------------------------------------------


# Program to validate scores, drop lowest, and calculate average + grade


# Step 1: Ask for number of scores
num_scores = int(input("How many scores do you want to enter? "))


# Step 2: Initialize empty list
score_list = []


# Step 3: Loop to collect scores
i = 1
while i <= num_scores:
    try:
        score = float(input(f"Enter score #{i}: "))
        if 0 <= score <= 100:
            score_list.append(score)
            i += 1
        else:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i} again:")
    except ValueError:
        print("Please enter a valid number.")

# Step 4: Process scores
lowest_score = min(score_list)
modified_list = score_list.copy()
modified_list.remove(lowest_score)
average = sum(modified_list) / len(modified_list)

# Step 5: Determine grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Step 6: Display results
print("\n-------------Results-------------")
print(f"Lowest Score   : {lowest_score}")
print(f"Modified List  : {modified_list}")
print(f"Scores Average : {average:.2f}")
print(f"Grade          : {grade}")
print("---------------------------------")


