my_list = [1, "a", True, [1, "2", "False"], {"int": 1, "str": "2", "bool": True}, {1, "2", True}, (1, "2", True), None]
my_type = [int, str, bool, list, dict, set, tuple, None]

for key, value in enumerate(my_list):
    result = "good" if type(value) == my_type[key] else "bad"
    print(f"{result}: {value} is {type(value)}")

