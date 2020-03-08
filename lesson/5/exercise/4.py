map_digits = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("4.txt", "r") as file_source, open("4_new.txt", "w+") as file_target:
    for line in file_source:
        first, second = line.split(" — ")
        file_target.write(f"{map_digits[first]} — {second}")

