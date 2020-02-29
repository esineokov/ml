my_list = list(input("Enter list: "))
for i in range(len(my_list)):
    if i == len(my_list)-1:
        break
    if not i % 2:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)
