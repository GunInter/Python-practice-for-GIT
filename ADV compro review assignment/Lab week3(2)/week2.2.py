"""**Assignment 2: If-Elif-Else Statement**
**Topic**: If-Else
**Objective**: Implement multiple conditions using if-elif-else statements.
1. Define an integer variable named `score` and assign it a value between 0 and 100.
2. Use an if-elif-else statement to print the grade based on the following criteria:
- 90-100: "A"
- 80-89: "B"
- 70-79: "C"
- 60-69: "D"
- Below 60: "F"
3. Test the function with different scores to show the result from A to F."""

score = 67  # six seven!!!!!!!!!!!!!!!!!!!!!

if score >= 90:
    print("Your grade is A")

elif score >= 80 and score <= 89:
    print("Your grade is B")

elif score >= 70 and score <= 79:
    print("Your grade is C")

elif score >= 60 and score <= 69:
    print("Your grade is D")

else:
    print("COngrats you sucks")
