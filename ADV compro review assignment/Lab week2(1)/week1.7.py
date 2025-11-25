'''Assignment 7: List sort() Method
Objective: Learn how to sort elements in a list using sort().

    1.    Create a list named scores containing the following numbers: 88, 92, 75, 89, 78.
    2.    Use the sort() method to sort the list in ascending order.
    3.    Print the sorted list.
    4.    Sort the list in descending order and print it.
    5.    Create a list of strings named names containing “Alice”, “Bob”, “Charlie”, “David”, “Eve” and sort it in alphabetical order.'''

num = [88, 92, 75, 89, 78]

num.sort()
print(num)

num.sort(reverse=True)
print(num)

name = ["Alice", "Bob", "Charlie", "David", "Eve"]
name.sort()
print(name)

name.sort(reverse=True)
print(name)
