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