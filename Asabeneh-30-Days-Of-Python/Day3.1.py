# 1.Declare your age as integer variable
age = 21
# 2.Declare your height as a float variable
height = 173.5
# 3.Declare a complex number variable
complex_num = 5 + 6j
# 4.Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
''' Enter base: 20
    Enter height: 10
    The area of the triangle is 100'''

tri_base = int(input('Enter base of triangle: '))
tri_height = int(input('Enter height of triangle: '))
print('The area of the triangle is ', 0.5 * tri_base * tri_height)
# 5.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is ', perimeter)
# 6.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lenght_rec = int(input('Enter lenght: '))
width_rec = int(input('Enter width: '))
area_rec = lenght_rec * width_rec
print(area_rec)
# 7.Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius_circle = int(input('Enter radius: '))
area_cir = 3.14 * radius_circle * radius_circle
cirumference = 2 * 3.14 * radius_circle
print('Area of circle is : ', area_cir)
print('CIrcumference of circle is: ', cirumference)
# 8.Calculate the slope, x-intercept and y-intercept of y = 2x -2
m1 = 2
y_intercept = -2
x_intercept = 1

print("Slope:", m1)
print("y-intercept:", y_intercept)
print("x-intercept:", x_intercept)

# 9.Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
y2, y1 = 2, 2
x2, x1 = 6, 10

m = (y2 - y1 / x2 - x1)
print("slope is : ", m)
# 10.Compare the slopes in tasks 8 and 9.
print("values compare between task 8 and 9", m1 == m)
# 11.Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
x = -5
y = x**2 + 6*x + 9
print("x =", x, "y =", y)

x = -4
y = x**2 + 6*x + 9
print("x =", x, "y =", y)

x = -3
y = x**2 + 6*x + 9
print("x =", x, "y =", y)

x = -2
y = x**2 + 6*x + 9
print("x =", x, "y =", y)
# 12.Find the length of 'python' and 'jargon' and make a falsy comparison statement.
print(len('python') != len('jargon'))
# 13.Use and operator to check if 'on' is found in both 'python' and 'jargon'
print('on' in 'python' and 'on' in 'jargon')
# 14.I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')
# 15.There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')
# 16.Find the length of the text python and convert the value to float and convert it to string
len_word = len('python')
float_convert = float(len_word)
string_convert = str(float_convert)
print(string_convert)
# 17.Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input('Pls enter num: '))
print(num % 2 == 0)
# 18.The floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division = 7 // 3
decimal = 2.7
covert_int = int(decimal)

print(floor_division == covert_int)
# 19.Check if type of '10' is equal to 10
print(type('10') == (type(10)))
# 20.Check if int('9.8') is equal to 10
numstr = '9.8'
numstr_float = float(numstr)

print(int(numstr_float) == 10)
# 21.Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
'''Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120'''
hours = int(input('Enter hours: '))
rate_per_hours = int(input('Enter rate per hour: '))
weekly_earning = hours * rate_per_hours
print('Your weekly earning is: ', weekly_earning)
# 22.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume someone lives up to hundred years
'''Enter number of years you have lived: 100
You have lived for 3153600000 seconds.'''
year = int(input('Enter number of years you have lived: '))
year_calculate = year * 365 * 24 * 60 * 60
print('You have lived for:', year_calculate, 'seconds')
# 23.Write a python script that displays the following table
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
