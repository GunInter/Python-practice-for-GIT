name = input("Enter ur mane pls ")
print(len(name))

if len(name) < 3:
    print("name must be at least 3 characthers")
elif len(name) > 50:
    print("maximum is 50 character")
else:
    print("ur name looks good na")
