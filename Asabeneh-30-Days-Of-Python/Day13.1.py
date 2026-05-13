# 1️⃣ Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# HINT:
# Use a condition inside list comprehension:
# [x for x in numbers if x <= 0]
negative_zero = [x for x in numbers if x <= 0]
print(negative_zero)

# 2️⃣ Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# HINT:
# You'll need 3 "for" loops in one line:
# [val for sub1 in list_of_lists for sub2 in sub1 for val in sub2]

flattened_list = [
    num for row in list_of_lists for inner in row for num in inner]
print(flattened_list)
# 3️⃣ Using list comprehension create the following list of tuples:
# [
# (0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# ...
# (10, 1, 10, 100, 1000, 10000, 100000)
# ]
# HINT:
# Each tuple is: (n, 1, n**1, n**2, n**3, n**4, n**5)
# Use a list comprehension that creates a tuple for each n in range(11).
squares = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(squares)


# 4️⃣ Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# ['FINLAND', 'HELSINKI', 'SWEDEN', 'STOCKHOLM', 'NORWAY', 'OSLO']
# HINT:
# You need two loops + .upper()
# [item.upper() for pair in countries for (item1, item2) in pair for item in (item1, item2)]
countries_list = [
    item.upper()                # convert each string to UPPERCASE
    for row in countries        # level 1
    for inners in row           # level 2
    for item in inners          # level 3 (tuple items)
]
print(countries_list)


# 5️⃣ Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
#  {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#  {'country': 'NORWAY', 'city': 'OSLO'}]

# HINT:
# Create dict inside a list comprehension:
# [{'country': c.upper(), 'city': t.upper()} ... ]
countries_dicts = [
    {'country': country.upper(), 'city': city.upper()}
    for row in countries
    for (country, city) in row
]

print(countries_dicts)


# 6️⃣ Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]

# output:
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
# HINT:
# Use f-string inside comprehension:
# [f"{first} {last}" for pair in names for (first, last) in pair]


# 7️⃣ Write a lambda function which can solve a slope or y-intercept of linear functions.
# (example: slope = (y2 - y1) / (x2 - x1))

# HINT:
# slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
# intercept = lambda x, y, m: y - m*x
