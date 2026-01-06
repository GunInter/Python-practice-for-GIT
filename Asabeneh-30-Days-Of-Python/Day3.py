age = 21  # 1
height = 174  # 2
complex_num = 5j - 6  # 3

tri_base = input("Enter base:")  # 4
tri_height = input("Enter base: ")

tri_height_float = float(tri_height)
tri_base_float = float(tri_base)

total_area = 0.5 * tri_base_float * tri_height_float
total_area_int = int(total_area)

print("The area of the triangle is : ", total_area_int)


a = input("Enter side a: ")
b = input("Enter side b: ")
c = input("Enter side c: ")

a_int = int(a)
b_int = int(b)
c_int = int(c)

total_perimeter = a_int + b_int + c_int

print("The perimeter of the triagle is", total_perimeter)
