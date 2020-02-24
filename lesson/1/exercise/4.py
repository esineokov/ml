var = input("Enter number: ")
var_len = len(var)
current = 0
max_ = 0

while current < var_len:
    item = int(var[current])
    if item == 9:
        max_ = item
        break
    else:
        if item > max_:
            max_ = item
    current += 1

print(f"Max digit: {max_}")

