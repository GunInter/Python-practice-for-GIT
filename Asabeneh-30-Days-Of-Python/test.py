fruits = ['banana', 'orange', 'mango', 'lemon']
# Get fruit from input
# If not in list → add it and print list
# Else → print "That fruit already exist in the list"
fruits_input = input('Pls enter fruit name:').capitalize()
if fruits_input in fruits:
    print('That fruit already exist in the list')
elif fruits_input not in fruits:
    fruits.append(fruits_input)
    print(fruits)
