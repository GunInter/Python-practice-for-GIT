first_name = "Nonpravit"
last_name = "Kachonnarongvanich"
full_name = "Nonpravit Kachonnarongvanich"
country = "Thailand"
city = "Bangkok"
age = 21
birth_year = 2004
is_married = False
is_true = True
is_light_on = True

first_name, last_name, full_name = "Nonpravit", "Kachonnarongvanich", "Nonpravit Kachonnarongvanich"

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(birth_year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))
print(len(last_name))
print("Is first name longer than last name?", len(first_name) > len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius_circle = 30
pi = 3.14
area_of_the_circle = pi * 30**2
circum_of_circle = 2 * pi * radius_circle

radius_input = input("Give the radius value: ")
radius_input_int = int(radius_input)
print(radius_input_int**2 * pi)
