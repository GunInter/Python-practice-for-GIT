'''
**Assignment 8: Using Break in a Loop**
**Topic**: Loops Flow Control
**Objective**: Understand how to use the break statement to exit a loop early.
1. Use a for loop to iterate over the numbers from 1 to 10 using range function.
2. Use a break statement to exit the loop when the number is 5.
3. Print the numbers iterated before the break.'''

i = 0
for i in range (1,11):
    if i == 5:
        break
    print(i)

