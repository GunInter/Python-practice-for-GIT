'''**Assignment 9: Using Continue in a Loop**
**Topic**: Loops Flow Control
**Objective**: Understand how to use the continue statement to skip iterations in a loop.
1. Use a for loop to iterate over the numbers from 1 to 10 using range function.
2. Apply a continue statement to skip the number 5.
3. Print number of each loop'''

i = 0
for i in range (1,11):
    if i == 5:
        continue
    print(i)