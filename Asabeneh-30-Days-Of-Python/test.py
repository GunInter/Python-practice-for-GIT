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
skills = person['skills']
mid = len(skills) // 2
if 'skills' in person:
    print(skills[mid])

# 7.2 Check if 'Python' is in skills
if 'Python' in skills:
    print('Python skill found')
# 7.3 Determine role:
# - JavaScript + React → front end
# - Node + Python + MongoDB → backend
# - React + Node + MongoDB → fullstack
# - else → unknown

# 7.4 If married and lives in Finland:
# print "Asabeneh Yetayeh lives in Finland. He is married."
married = person['is_marred']
live_country = person['country']

if married is True and live_country is 'Finland':
    print("Asabeneh Yetayeh lives in Finland. He is married.")
