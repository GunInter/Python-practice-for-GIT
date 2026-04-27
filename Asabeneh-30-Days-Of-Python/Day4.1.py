# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string.
word1 = 'Thirty'
word2 = 'Day'
word3 = 'Of'
word4 = 'Python'
combine = word1 + word2 + word3 + word4
print(combine)

# 2. Concatenate the string 'Coding', 'For', 'All' to a single string.
coding = 'Coding'
for_ = 'For'
All = 'All'
combine1 = coding + for_ + All
print(combine1)

# 3. Declare a variable named company and assign it "Coding For All".
company = 'Coding For All'
# 4. Print the variable company using print().
print(company)
# 5. Print the length of the company string using len().
print(len(company))
# 6. Change all characters to uppercase using upper().
print(company.upper())
# 7. Change all characters to lowercase using lower().
print(company.lower())
# 8. Use capitalize(), title(), swapcase() on "Coding For All".
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9. Slice out the first word of "Coding For All".
slice_company = company[6:14]
print(slice_company)
# 10. Check if "Coding For All" contains the word "Coding".
print('Coding' in company)
# 11. Replace "Coding" with "Python" in "Coding For All".
print(company.replace('Coding', 'Python'))

# 12. Change "Python for Everyone" to "Python for All".
word5 = 'Python for everyone'
print(word5.replace('Everyone', 'All'))
# 13. Split the string "Coding For All" using space.
print(company.split(' '))
# 14. Split "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" by comma.
list_company = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(list_company.split(', '))
# 15. What is the character at index 0 in "Coding For All"?
first_letter = company[0]
print(first_letter)
# 16. What is the last index of "Coding For All"?
last_letter = company[-1]
print(last_letter)
# 17. What character is at index 10 in "Coding For All"?
ten_letter = company[10]
print(ten_letter)
# 18. Create an acronym for "Python For Everyone".
word5_firstCha = word5[0]
word5_SecondCha = word5[7]
word5_ThirdCha = word5[11]
acronym = word5_firstCha + word5_SecondCha + word5_ThirdCha
print(acronym)
# 19. Create an acronym for "Coding For All".
company_1 = company[0]
company_2 = company[7]
company_3 = company[11]
acronym1 = company_1 + company_2 + company_3
print(acronym1)
# 20. Find position of first occurrence of 'C' in "Coding For All".
find_pos = 'C'
print(company.index(find_pos))
# 21. Find position of first occurrence of 'F' in "Coding For All".
find_pos1 = 'F'
print(company.index(find_pos1))
# 22. Use rfind to find last occurrence of 'l' in "Coding For All People".
find_pos2 = 'l'
print(company.index(find_pos2))
# 23. Find position of first occurrence of "because" in:
# "You cannot end a sentence with because because because is a conjunction"
occurrenc_pos = "You cannot end a sentence with because because because is a conjunction"
print(occurrenc_pos.find('because'))

# 24. Use rindex to find last occurrence of "because" in the same sentence.
print(occurrenc_pos.rindex('because'))
# 25. Slice out "because because because" from the sentence.
print(occurrenc_pos[31:55])
'''sentence = "You cannot end a sentence with because because because is a conjunction"

start = sentence.find('because')
end = start + len('because because because')

print(sentence[start:end])'''

# 26. Find again the first occurrence of "because" (repeat practice).
print(occurrenc_pos.find('because'))
# 27. Slice out "because because because" again (repeat practice).
start = occurrenc_pos.find('because')
end = start + len('because because because')
# 28. Check if "Coding For All" starts with "Coding".
print(company.startswith('Coding'))
# 29. Check if "Coding For All" ends with "coding".
print(company.endswith('Coding'))
# 30. Remove spaces from "   Coding For All      ".
sentence = "   Coding For All      "
print(sentence.strip(' '))
# 31. Which of these is a valid identifier using isidentifier():
# - 30DaysOfPython
# - thirty_days_of_python
challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True

# 32. Join ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] with " # ".
vocab = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(vocab)
print(result)
# 33. Use newline escape sequence to print:
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge. \nI just wonder what is next.')
# 34. Use tab escape sequence to format:
# Name      Age     Country
# Asabeneh  250     Finland

# 35. Format string:
# radius = 10
# area = 3.14 * radius ** 2
# Output: The area of a circle with radius 10 is 314 meters square.

# 36. Format the following operations:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
