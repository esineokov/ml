a = float(input("Enter start: "))
b = float(input("Enter finish: "))

day = 1
current = a

while current < b:
    day += 1
    current = current + current*0.1

print(f"You will reach the result on the {day}th day")

