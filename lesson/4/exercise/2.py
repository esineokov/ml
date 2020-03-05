import random

my_list = [random.randint(1, 10) for i in range(10)]
print(f"Original random list: {my_list}")

my_new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(f"Edited list: {my_new_list}")