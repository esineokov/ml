import random

with open("5.txt", "w+") as file:
    for i in range(10):
        file.write(f"{random.randint(1, 10)} ")

    file.seek(0)

    digits = file.readline().strip().split()
    digits = map(int, digits)

    print(sum(digits))

