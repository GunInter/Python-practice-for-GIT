weight = input('weight: ')
choose_unit = input("(L)bs or (K)g: ")

if choose_unit == "K":
    weight_pounds = int(weight) * 2.5
    print(weight_pounds)

elif choose_unit == "L":
    weight_kilograms = int(weight) / 2.5
    print(weight_kilograms)
