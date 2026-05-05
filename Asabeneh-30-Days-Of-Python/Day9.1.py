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

your_age = int(input('Enter your age: '))
my_age = 18
if your_age > my_age:
    num1 = your_age - my_age
    print('You are ', num1, 'years older than me.')

elif your_age < my_age:
    num2 = my_age - your_age
    print('You are ', num2, 'years younger than me.')

elif your_age == my_age:
    print('Our age r equal')


# 3. Compare two numbers
# Get a and b from input
# If a > b → print "a is greater than b"
# If a < b → print "a is smaller than b"
# Else → print "a is equal to b"
A = int(input('Enter number one: '))
B = int(input('Enter number two: '))

if A > B:
    print(A, 'is greater than', B)
elif B > A:
    print(B, 'is greater than', A)
else:
    print(A, 'is equal to', B)
# 4. Grade system
# Get score from input
# 80–100 → A
# 70–89 → B
# 60–69 → C
# 50–59 → D
# 0–49 → F
score = int(input('Enter your score: '))
if score <= 49:
    print('You get F')
elif 50 <= score <= 59:
    print('You get D')
elif 60 <= score <= 69:
    print('You get C')
elif 70 <= score <= 79:
    print('You get B')
elif 80 <= score <= 100:
    print('You get A')
# 5. Season checker
# Get month from input
# Autumn → September, October, November
# Winter → December, January, February
# Spring → March, April, May
# Summer → June, July, August

Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']

month = input('Enter month:').capitalize()
if month in Autumn:
    print('U r in Autumn season')
elif month in Winter:
    print('U r in Winter season')
elif month in Spring:
    print('U r in Spring season')
elif month in Summer:
    print('U r in Summer season')

# 6
fruits = ['banana', 'orange', 'mango', 'lemon']
# Get fruit from input
# If not in list → add it and print list
# Else → print "That fruit already exist in the list"
fruits_input = input('Pls enter fruit name:')
if fruits_input in fruits:
    print('That fruit already exist in the list')
elif fruits_input not in fruits:
    add = fruits.append(fruits_input)
    print(add)
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
