var_int = 123
var_str = "abc"
var_list = [var_int, var_str]
var_dict = {'v1': var_int, 'v2': var_str, 'v3': var_list}
var_tuple = (var_int, var_str, var_list, var_dict)

print("Look at some types of variables:")
print(f"int: {var_int}")
print(f"str: {var_str}")
print(f"list: {var_list}")
print(f"dict: {var_dict}")
print(f"tuple: {var_tuple}")

print("\nEnter data:")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")

print(f"\nI think you name is {first_name} {last_name}. You are {age} years old. And your height is {height}")


