'''Assignment 10: Dictionary Basics
Objective: Learn how to create and use dictionaries in Python.

    1.    Create a dictionary named student with keys: “name”, “age”, “grade”.
    2.    Set the values of the dictionary to your name, age, and a grade of your choice.
    3.    Print the dictionary.
    4.    Add a new key-value pair: “school” with the value of your school name.
    5.    Remove the key “grade” from the dictionary and print the updated dictionary.'''

student = {

    "name": "Nonpravit",
    "age": 20,
    "grade": "B+",

}
print(student)

student["university"] = "KMITL-university"
del student["grade"]

print(student)
