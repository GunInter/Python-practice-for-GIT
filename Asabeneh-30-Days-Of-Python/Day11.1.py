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


def print_list(lst):
    for item in lst:
        print(item)


names = ['Gun', 'Alice', 'Bob', 'Charlie', 'David']
print_list(names)

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


print(reverse_list(num_list))
# 10.Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(lst):
    capitalize_items = []

    for item in lst:
        capitalize_items.append(item.capitalize())  # capitalize each string
    return capitalize_items


print(capitalize_list_items(['apple', 'banana', 'mango']))

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# Example:
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))


def add_item(lst, item):
    lst.append(item)

    return lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']

print(add_item(food_staff, 'Meat'))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# Example:
# remove_item(food_staff, 'Mango')


def remove_item(lst, item):
    lst.remove(item)
    return lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# Example:
# sum_of_numbers(5) -> 15


def sum_of_numbers(sum_num):
    total = 0
    num_sum = 1

    while num_sum <= sum_num:

        total = total + num_sum
        num_sum = num_sum + 1

    return total


print(sum_of_numbers(6))

# 14. Write sum_of_odds(num)


def sum_of_odds(odd_num):
    total_odd = 0
    current = 0

    while current <= odd_num:
        if current % 2 != 0:
            total_odd = total_odd + current
        current = current + 1

    return total_odd


print(sum_of_odds(25))

# 15. Write sum_of_even(num)


def sum_of_evens(even_num):
    total_even = 0
    current_even = 0

    while current_even <= even_num:
        if current_even % 2 == 0:
            total_even = total_even + current_even
        current_even = current_even + 1

    return total_even


print(sum_of_evens(25))
# 16. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
# example
# print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.


def evens_and_odds(num):
    evens = 0
    odds = 0
    current = 0

    while current <= num:
        if current % 2 == 0:
            evens = evens + 1
        else:
            odds = odds + 1
        current = current + 1

    print("The number of odds are", odds)
    print("The number of evens are", evens)

# 17. Write factorial(num)\ Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number


def factorial(num):
    total = 1
    counter = num
    while counter > 0:
        total = total * counter
        counter = counter - 1
    return total


print(factorial(4))
# 18. Write is_empty(value)\Call your function is_empty, it takes a parameter and it checks if it is empty or not


def is_empty(value):
    if value == "":
        print('its empty')
    else:
        print('its not empty')


print(is_empty(' '))
# 19. Write:
# calculate_mean(lst)
# calculate_median(lst)
# calculate_mode(lst)
# calculate_range(lst)
# calculate_variance(lst)
# calculate_std(lst)


def calculate_mean(lst):
    total = 0
    for mean in lst:
        total = total + mean
    mean = total / len(lst)
    return mean


print(calculate_mean([2, 4, 6, 8]))


def calculate_median(lst):
    pass


def calculate_mode(lst):
    pass


def calculate_range(lst):
    pass


def calculate_variance(lst):
    pass


def calculate_std(lst):
    pass

# 20. Write is_prime(num)

# 21. Check if all items are unique in list

# 22. Check if all items are same data type

# 23. Check if variable name is valid python variable

# 24. Most spoken languages (requires countries-data.py)

# 25. Most populated countries (requires countries-data.py)
