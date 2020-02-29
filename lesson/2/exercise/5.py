rating_list = [7, 5, 3, 3, 2]
while True:
    number = int(input("Enter rating: "))
    for key, value in enumerate(rating_list):
        if key == len(rating_list)-1:
            rating_list.append(number)
            break
        if number > value:
            rating_list.insert(key, number)
            break
        else:
            continue
    print(rating_list)
