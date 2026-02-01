# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

first = "Thirty"
second = "Days"
third = "Of"
fourth = "Python"
space = " "
merge = first + space + second + space + third + space + fourth

print(merge)

# 2 Concatenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'.

a = 'Coding'
b = 'For'
c = 'All'

merge1 = a + space + b + space + c
print(merge1)

# 3 Declare a variable named company and assign it to an initial value "Coding For All".

company = merge1

# 4 Print the variable company using print().

print(company)

# 5 Print the length of the company string using len() method and print().

print(len(company))

# 6 Change all the characters to capital letters using upper() method.

print(company.upper())

# 7 Change all the characters to lowercase letters using lower() method.

print(company.lower())

# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 Cut (slice) out the first word of Coding For All string.

remove_first_word = company[6:]
print(remove_first_word)

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.startswith('Coding'))


# 11 Replace the word coding in the string 'Coding For All' to Python.

print(company.replace('Coding','Python'))

# 12 Change Python for Everyone to Python for All using the replace method or other methods.

p_for_all = 'Python for Everyone'
print(p_for_all.replace('Everyone','All'))

# 13 Split the string 'Coding For All' using space as the separator (split()).

print(company.split(' '))

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

stocks = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(stocks.split(','))

# 15 What is the character at index 0 in the string Coding For All.

first_letter = company[0]
print(first_letter)

# 16 What is the last index of the string Coding For All.

last_letter = company[13]
print(last_letter)

# 17 What character is at index 10 in "Coding For All" string.

tenth_letter = company[10]
print(tenth_letter)


# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.



# 19 Create an acronym or an abbreviation for the name 'Coding For All'.

# 20 Use index to determine the position of the first occurrence of C in Coding For All.

# 21 Use index to determine the position of the first occurrence of F in Coding For All.

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.

# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
#   'You cannot end a sentence with because because because is a conjunction'

# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence:
#   'You cannot end a sentence with because because because is a conjunction'

# 25 Slice out the phrase 'because because because' in the following sentence:
#   'You cannot end a sentence with because because because is a conjunction'

# 26 Find the position of the first occurrence of the word 'because' in the following sentence:
#   'You cannot end a sentence with because because because is a conjunction'

# 27 Slice out the phrase 'because because because' in the following sentence:
#   'You cannot end a sentence with because because because is a conjunction'

# 28 Does 'Coding For All' start with a substring Coding?

# 29 Does 'Coding For All' end with a substring coding?

# 30 '   Coding For All      ' remove the left and right trailing spaces in the given string.

# 31 Which one of the following variables return True when we use the method isidentifier():
#   30DaysOfPython
#   thirty_days_of_python

# 32 The following list contains the names of some Python libraries:
#   ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
#   Join the list with a hash and space string.
