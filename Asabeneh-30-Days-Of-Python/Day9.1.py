# if-else exercises

# 1. Age check (driving eligibility)
# Get user input
# If age >= 18 → print "You are old enough to learn to drive."
# Else → print how many years left

driver_age = int(input('Enter your age: '))

if driver_age >= 18:
    print('You are old enough to learn to drive.')

else:
    num = 18 - driver_age
    print('You need', num, 'more years to learn to drive.')

# 2. Compare my_age and your_age
# my_age = ?
# Get your_age from input
# Compare and print:
# - who is older
# - use "year" or "years" correctly
# - if equal → custom message

# 3. Compare two numbers
# Get a and b from input
# If a > b → print "a is greater than b"
# If a < b → print "a is smaller than b"
# Else → print "a is equal to b"

# 4. Grade system
# Get score from input
# 80–100 → A
# 70–89 → B
# 60–69 → C
# 50–59 → D
# 0–49 → F

# 5. Season checker
# Get month from input
# Autumn → September, October, November
# Winter → December, January, February
# Spring → March, April, May
# Summer → June, July, August

# 6. Fruit checker
fruits = ['banana', 'orange', 'mango', 'lemon']
# Get fruit from input
# If not in list → add it and print list
# Else → print "That fruit already exist in the list"

# 7. Person dictionary tasks
person = {
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

# 7.1 Check if 'skills' key exists
# If yes → print middle skill

# 7.2 Check if 'Python' is in skills

# 7.3 Determine role:
# - JavaScript + React → front end
# - Node + Python + MongoDB → backend
# - React + Node + MongoDB → fullstack
# - else → unknown

# 7.4 If married and lives in Finland:
# print "Asabeneh Yetayeh lives in Finland. He is married."
