seasons = {"winter": [12, 1, 2], "spring": [3, 4, 5], "summer": [6, 7, 8], "autumn": [9, 10, 11]}

while True:
    number = int(input("Enter month: "))
    if 1 <= number <= 12:
        break
    print("The value must be between 1 and 12")

for key, value in seasons.items():
    if number in value:
        print(f"This is {key}")
