'''Assignment 9: List Slicing
Objective: Learn how to slice lists to access sublists.

    1.    Create a list named letters containing the first 10 letters of the alphabet. Ex. [A, B, C, D, ... ]
    2.    Slice the list to get the first 5 letters and print the result.
    3.    Slice the list to get the last 5 letters and print the result.
    4.    Reverse the list and print the result.'''

letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
slice_first_letter = letter[0:5]
print(slice_first_letter)

slice_last_letter = letter[5:10]
print(slice_last_letter)

reversed_letter = letter[::-1]
print(reversed_letter)
