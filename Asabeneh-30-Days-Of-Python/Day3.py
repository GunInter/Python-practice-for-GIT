age = 21  # 1 Declare your age as integer variable
height = 174.0  # 2 Declare your height as a float variable
complex_num = 5j - 6  # 3 Declare a complex number variable

# 4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# Enter base: 20
# Enter height: 10
# The area of the triangle is 100

tri_base = input("Enter base:")
tri_height = input("Enter height: ")

tri_height_float = float(tri_height)
tri_base_float = float(tri_base)

total_area = 0.5 * tri_base_float * tri_height_float
total_area_int = int(total_area)

print("The area of the triangle is : ", total_area_int)

# 5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12

a = input("Enter side a: ")
b = input("Enter side b: ")
c = input("Enter side c: ")

a_int = int(a)
b_int = int(b)
c_int = int(c)

total_perimeter = a_int + b_int + c_int

print("The perimeter of the triagle is", total_perimeter)

# 6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

lenght_rec = float(input("Enter the length: "))
width_rec = float(input("Enter the width: "))

area_rec = lenght_rec * width_rec
perimeter_rec = 2 * (lenght_rec + width_rec)

print(area_rec)
print(perimeter_rec)

# 7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius_cir = float(input("Enter the radius: "))
pi = 3.14

area_cir = radius_cir * radius_cir * pi
circum = 2 * pi * radius_cir
print(area_cir)
print(circum)
# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2

m1 = 2
y_intercept = -2
x_intercept = 1

print("Slope:", m1)
print("y-intercept:", y_intercept)
print("x-intercept:", x_intercept)

# 9 Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10

m = (y2 - y1 / x2 - x1)
print("slope is : ", m)

# 10 Compare the slopes in tasks 8 and 9.

print("values compare between task 8 and 9", m1 == m)


# 11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.

# Equation: y = x^2 + 6x + 9

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


# 12 Find the length of 'python' and 'jargon' and make a falsy comparison statement.

print("Word python and jargon is not equal alphabets:",
      len("python") != len("jargon"))

# 13 Use and operator to check if 'on' is found in both 'python' and 'jargon'

print('on in python and jargon', 'on' in 'python' and 'on' in 'jargon')

# 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print("check if jargon is in the sentence(I hope this course is not full of jargon)",
      'jargon' in 'I hope this course is not full of jargon')

# 15 There is no 'on' in both dragon and python

print('no on in python and dragon', not ('on' in 'dragon' and 'on' in 'python'))

#16 Find the length of the text python and convert the value to float and convert it to string



#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?