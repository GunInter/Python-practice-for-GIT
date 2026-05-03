# sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Nvdia','TSMC','AMD'])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

# 5. What is the difference between remove and discard
#Ans. remove() if it cant find value ,it will show error, Discard() doesnt raise error
# remove() raises error if item not found
# discard() does nothing if item not found

# 6. Join A and B
C = A.union(B)
print(C)

# 7. Find A intersection B
intersection = A.intersection(B)
print(intersection)
# 8. Is A subset of B
subset = A.issubset(B)
print(subset)
# 9. Are A and B disjoint sets
disjoint = B.isdisjoint(A)
print(disjoint)
# 10. Join A with B and B with A
AB = A.union(B)
BA = B.union(A)
print(AB)
print(BA)
# 11. What is the symmetric difference between A and B
sym = A.symmetric_difference(B)
print(sym)
# 12. Delete the sets completely
del it_companies  
del A  
del B
# 13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
convert_set = set(age)
print(len(age))
print(len(convert_set))
print(len(age)>(len(convert_set)))

# 14. Explain the difference between the following data types: string, list, tuple and set
#string word value
#list can chnage convert and modify
#tuple cant modify
#set uniqe value

# string: sequence of characters (text)
# list: ordered, mutable (can change)
# tuple: ordered, immutable (cannot change)
# set: unordered, unique values only (no duplicates)
# 15. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?

word = 'I am a teacher and I love to inspire and teach people'
split = word.split()
unique_words = set(split)
lenght_words = len(unique_words)
print(lenght_words)

