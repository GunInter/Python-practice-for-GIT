# ...existing code...
phone = input('Phone: ')

storage = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
}

output = ""

for ch in phone:
    output += storage.get(ch, "!")

print(output)
# ...existing code...
