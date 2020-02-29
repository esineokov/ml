def my_division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You cannot divide by zero")
        return None


first = input("First number: ")
second = input("Second number: ")

try:
    first, second = float(first), float(second)
except ValueError:
    print("Only numbers are allowed")

result = my_division(first, second)
if result:
    print(result)
