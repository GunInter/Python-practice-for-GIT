# 1. Create an empty tuple
empty_tuple = ()
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
siblings_sisters = ('Hee','Por','Cartoon')
siblings_brother = ('Parn','Nano','August')
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = siblings_brother + siblings_sisters 
# 4. How many siblings do you have?
print('I have',(len(siblings)),'siblings')
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father_mother = ('Vikit','Lhee')
family_members = siblings + father_mother
print(family_members)
# 6. Unpack siblings and parents from family_members
sib1, sib2 , sib3,sib4,sib5,sib6, parent1,parent2 = family_members
*siblings_only, parent1, parent2 = family_members
print(sib1)
print(sib2)
print(sib3)
print(sib4)
print(sib5)
print(sib6)
print(parent1)
print(parent2)

# 7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff
fruits = ('apple', 'banana', 'orange', 'mango', 'grape')

vegetables = ('carrot', 'broccoli', 'spinach', 'potato', 'tomato')

animal_products = ('milk', 'egg', 'cheese', 'butter', 'yogurt')

food_stuff = fruits + vegetables + animal_products
print(food_stuff)
# 8. Slice out the middle item or items from the food_stuff tuple
Middle_items =food_stuff[len(food_stuff)//2]
print(Middle_items)
# 9. Slice out the first three items and the last three items from food_stuff tuple
first_3items = food_stuff[0:3]
last_3items = food_stuff[-3:]
print(first_3items)
print(last_3items)
# 10. Delete the food_stuff tuple completely
del food_stuff
# 11. Check if an item exists in a tuple:
#     - Check if 'Estonia' is a nordic country
#     - Check if 'Iceland' is a nordic country
#     nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)