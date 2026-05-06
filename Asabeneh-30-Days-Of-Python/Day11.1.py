# functions exercises

# 1. Declare a function add_two_numbers.
# It takes two parameters and returns a sum.
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(3, 5))

# 2. Write a function area_of_circle.
# area = π * r * r


def circle_area(r):

    area = 3.14 * r * r
    return area


print(circle_area(5))

# 3. Write a function add_all_nums
# Takes arbitrary number of arguments
# Sum all numbers
# If non-number exists → print feedback


def add_all_nums(*addall):
    total = 0
    for sum in addall:
        total += sum
    return total


print(add_all_nums(2, 3, 5))
# 4. Convert Celsius to Fahrenheit
# °F = (°C x 9/5) + 32


def cel_to_fahren(C):

    F = (C * 9/5) + 32
    return F


print(cel_to_fahren(35))

# 5. Write check_season(month)
# Return: Autumn, Winter, Spring or Summer

# 6. Write calculate_slope

# 7. Write solve_quadratic_eqn(a, b, c)

# 8. Write print_list(lst)
# Print each element using loop

# 9. Write reverse_list(lst)
# Reverse using loops (not reverse())

# Example:
# print(reverse_list([1,2,3,4,5]))
# [5,4,3,2,1]

# 10. Write capitalize_list_items(lst)
# Return capitalized items list

# 11. Write add_item(lst, item)
# Add item to end of list

# Example:
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))

# 12. Write remove_item(lst, item)
# Remove item from list

# Example:
# remove_item(food_staff, 'Mango')

# 13. Write sum_of_numbers(num)
# Sum all numbers from 0 to num

# Example:
# sum_of_numbers(5) -> 15

# 14. Write sum_of_odds(num)

# 15. Write sum_of_even(num)

# 16. Write evens_and_odds(num)
# Count total evens and odds

# Example:
# evens_and_odds(100)

# 17. Write factorial(num)

# 18. Write is_empty(value)

# 19. Write:
# calculate_mean(lst)
# calculate_median(lst)
# calculate_mode(lst)
# calculate_range(lst)
# calculate_variance(lst)
# calculate_std(lst)

# 20. Write is_prime(num)

# 21. Check if all items are unique in list

# 22. Check if all items are same data type

# 23. Check if variable name is valid python variable

# 24. Most spoken languages (requires countries-data.py)

# 25. Most populated countries (requires countries-data.py)
