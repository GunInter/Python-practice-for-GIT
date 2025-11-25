'''Assignment 6: List pop() Method
Objective: Understand how to remove elements from a list using pop() and how to use the removed elements.
    1.    Create a list named cities containing “New York”, “Los Angeles”, “Chicago”, “Houston”, “Phoenix”.
    2.    Use the pop() method to remove the last element from the list and store it in a variable.
    3.    Print the variable holding the removed element.
    4.    Use pop() to remove the first element from the list.
    5.    Print the final list of cities.
    '''
city = ["New York", "Los Angles", "Chicago", "Houston", "Phoenix"]
last_city = city.pop()

print(last_city)
print(city)

first_city = city.pop(0)
print(first_city)
