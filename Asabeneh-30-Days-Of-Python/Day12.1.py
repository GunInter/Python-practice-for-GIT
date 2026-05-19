#1.Writ a function which generates a six digit/character random_user_id.
  #print(random_user_id());
  #'1ee33d'

import random
import string   
def random_user_id():

    user_id = ""
    string_combine_random = string.digits + string.ascii_letters

    for i in range(6):
        user_id += random.choice(string_combine_random)
    return user_id


print(random_user_id())

#2.Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.


#user_id_gen_by_user() # user input: 5 5 #output: #kcsy2 #SMFYb #bWmeq #ZXOYh #2Rgxf
#user_id_gen_by_user() # 16 5 #1GCSgPLMaBAVQZ26 #YD7eFwNQKNs7qXaT #ycArC5yrRupyG00S #UbGxOFI7UXSWAyKN #dIV0SSUTgAdKwStr

import random
import string   

def random_user_id():
    user_id = ""
    string_combine_random = string.digits + string.ascii_letters

    for i in range(6):
        user_id += random.choice(string_combine_random)
    return user_id

print(random_user_id())


#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

#print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f"rgb({r},{g},{b})"

# 4.Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n):
    hex_colors = []
    hex_digits = string.digits + 'abcdef'

    for _ in range(n):
        color = '#'
        for _ in range(6):
            color += random.choice(hex_digits)
        hex_colors.append(color)

    return hex_colors

print(list_of_hexa_colors(5))
#5.Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors():
    number = int(input("Enter number of RGB colors: "))
    colors = []

    for _ in range(number):
        colors.append(rgb_color_gen())

    return colors

#6.Write a function generate_colors which can generate any number of hexa or rgb colors.
 #generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
 #generate_colors('hexa', 1) # ['#b334ef']
 #generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
 #generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def generate_colors(color_type, number):
    if color_type == 'hexa':
        return list_of_hexa_colors(number)
    elif color_type == 'rgb':
        return list_of_rgb_colors()
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
    
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))    

#7.Write a function shuffle_list which takes a list as a parameter and returns a shuffled list.

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

#8.Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def unique_random_numbers():
    num_set = []
    while len(num_set) < 7:
        num = random.randint(0, 9)
        if num not in num_set:
            num_set.append(num)
    return num_set