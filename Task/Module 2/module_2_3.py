my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

y = 0
while y < len(my_list):
    if my_list[y] == 0:
        y += 1
        continue
    if my_list[y] < 0:
        break
    print(my_list[y])
    y += 1