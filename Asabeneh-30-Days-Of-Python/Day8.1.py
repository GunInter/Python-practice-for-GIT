# dictionaries

# 1. Create an empty dictionary called dog
dog = {}
# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name: '] = 'Bug'
dog['color: '] = 'Blue'
dog['breed: '] = 'Wolf'
dog['legs: '] = 4
dog['age: '] = 2
print(dog)
# 3. Create a student dictionary and add:
# first_name, last_name, gender, age, marital status, skills, country, city and address
student = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 4. Get the length of the student dictionary
print(len(student))
# 5. Get the value of skills and check the data type (should be a list)
print(student['skills'])
print(type(student['skills']))
# 6. Modify the skills values by adding one or two skills
student['skills'].append('C++')
print(student)
# 7. Get the dictionary keys as a list
keys_as_list = list(student.keys())
print(keys_as_list)
# 8. Get the dictionary values as a list
values_as_list = list(student.values())
print(values_as_list)
# 9. Change the dictionary to a list of tuples using items() method
print(student.items())
# 10. Delete one of the items in the dictionary
del student['first_name']
# 11. Delete one of the dictionaries
del student
