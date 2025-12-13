num = [1, 2, 2, 6, 5, 8, 4, 4, 9, 41, 10, 6, 7, 5]
nodup_num = []

for remove in num:
    if remove not in nodup_num:
        nodup_num.append(remove)


print(nodup_num)
