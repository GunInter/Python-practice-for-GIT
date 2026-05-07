# functions exercises

# 1. Declare a function add_two_numbers.
# It takes two parameters and returns a sum.
import math


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


def check_season(month):

    Autumn = ['September', 'October', 'November']
    Winter = ['December', 'January', 'February']
    Spring = ['March', 'April', 'May']
    Summer = ['June', 'July', 'August']

    if month in Autumn:
        return 'Autumn'

    elif month in Winter:
        return 'Winter'

    elif month in Spring:
        return 'Spring'

    elif month in Summer:
        return 'Summer'


print(check_season('September'))

# 6. Write a function called calculate_slope which return the slope of a linear equation


def calculate_slope(x1, y1, x2, y2):

    m = (y2 - y1) / (x2 - x1)
    return (m)


print(calculate_slope(1, 5, 6, 7))

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.


def solve_quadratic_eqn(a, b, c):

    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

    return x1, x2


print(solve_quadratic_eqn(1, -5, 6))

# 8.Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


def print_list():
    names = ['Gun', 'Alice', 'Bob', 'Charlie', 'David']
    for name in names:
        print(name)
    return (name)


print(print_list)

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# Example:
# print(reverse_list([1,2,3,4,5]))
# [5,4,3,2,1]

num_list = [1, 2, 3, 4, 5]


def reverse_list(lst):

    reversed_list = []

    for numm in lst:
        reversed_list.insert(0, numm)
    return reversed_list


print(reversed_list(num_list))
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
