'''**Assignment 4: Short-Hand If-Else with List Elements**
**Topic**: Short-Hand If-Else
**Objective**: Use short-hand if-else statements to modify list elements.
1. Create a list named `numbers` containing a integers from 1 to 5.
2. Use a list comprehension with a short-hand if-else statement to create a new list named `modified_numbers` 
where each element is increased by 10 if it is even, or decreased by 1 if it is odd.
3. Print the `modified_numbers` list.
4. The number line of code should limit to 3 lines only.
ex. numbers = [1, 2, 3, 4, 5]
modified_numbers will be [0, 12, 2, 14, 4]'''

number = [1, 2, 3, 4, 5]
modified_number = [x + 10 if x % 2 == 0 else x - 1 for x in number]

print(modified_number)
