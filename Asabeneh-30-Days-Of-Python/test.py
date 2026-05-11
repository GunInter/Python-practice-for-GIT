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


print(random_user_id)

#2.Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.


#user_id_gen_by_user() # user input: 5 5 #output: #kcsy2 #SMFYb #bWmeq #ZXOYh #2Rgxf
#user_id_gen_by_user() # 16 5 #1GCSgPLMaBAVQZ26 #YD7eFwNQKNs7qXaT #ycArC5yrRupyG00S #UbGxOFI7UXSWAyKN #dIV0SSUTgAdKwStr

def user_id_gen_by_user():
    
    user_id = ""
    string_combine_random = string.digits + string.ascii_letters
    user_ids = []
    input_num = input('Enter the number of characters and the number of IDs to be generated (separated by a space): ')

    for j in range(int(input_num.split()[1])):
        user_id = ""
        for i in range(int(input_num.split()[0])):
            user_id += random.choice(string_combine_random)
        user_ids.append(user_id)
    return user_ids
    
print(user_id_gen_by_user())


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
def list_of_hexa_colors():
    hex_colors = []
    hex_digits = string.digits + 'abcdef'

    for i in range(5):
        color = '#'
        for j in range(6):
            color += random.choice(hex_digits)
        hex_colors.append(color)
    return hex_colors

print(list_of_hexa_colors(5))
#5.Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def list_of_rgb_colors():

    number_rgb_color = int(input('Enter the number of RGB colors to be generated: '))

    for i in range(number_rgb_color):
        print(rgb_color_gen())
