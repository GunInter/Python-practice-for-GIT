# loops exercises

# 1. Iterate 0 to 10 using for loop
for number in range(11):
    print(number)
# 2. Iterate 0 to 10 using while loop
count = 0
while count < 11:
    print(count)
    count = count + 1
# 3. Iterate 10 to 0 using for loop
for number in range(10, -1, -1):
    print(number)
# 4. Iterate 10 to 0 using while loop
count = 10
while count >= 0:
    print(count)
    count = count - 1
# 5. Print triangle pattern:
# #
# ##
# ###
# ####
# #####
# ######
# #######
count_hash = 1
while count_hash <= 7:
    print(count_hash * '#')
    count_hash = count_hash + 1
# 6. Nested loop pattern (8x8 grid)
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for matrix in range(8):

    for line in range(7):
        print('#', end=' ')

    print('#', end='\n')


# 7. Print multiplication squares:
# 0 x 0 = 0
# ...
# 10 x 10 = 100
multi_count = 0
while multi_count <= 10:
    print(multi_count, 'x', multi_count, '=', multi_count * multi_count)
    multi_count = multi_count + 1

# 8. Iterate list and print items
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for program in lst:
    print(program)

# 9. Print even numbers from 0 to 100
even_num = 0
while even_num <= 100:
    if even_num % 2 == 0:
        print(even_num)
    even_num = even_num + 1

# 10. Print odd numbers from 0 to 100
odd_num = 0
while odd_num <= 100:
    if odd_num % 2 != 0:
        print(odd_num)
    odd_num = odd_num + 1

# 11. Print sum of all numbers from 0 to 100
sum_num = 0
sum = 0
while sum_num <= 100:
    sum = sum + sum_num
    sum_num = sum_num + 1
print('total of sum of 100 is:', sum)

# 12. Print sum of evens and odds separately
odd_num = 0
odd_total = 0
while odd_num <= 100:

    if odd_num % 2 == 0:

        odd_total = odd_total + odd_num
    odd_num = odd_num + 1

print(odd_total)


even_num = 0
even_total = 0
while even_num <= 100:

    if even_num % 2 == 0:

        even_total = even_total + even_num
    even_num = even_num + 1

print(even_total)

# 13. Loop countries and find those containing 'land'
# (you can mock a list if no file)

countries = [
    'Finland',
    'Sweden',
    'Iceland',
    'Thailand',
    'Norway',
    'Denmark',
    'Poland',
    'France'
]

for find_land in countries:
    if 'land' in countries:
        print('there is land is country list')

# 14. Reverse fruit list using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
