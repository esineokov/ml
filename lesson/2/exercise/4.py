words = input("Enter some words: ")

for key, value in enumerate(words.split()):
    print(f"{key} {value[:10]}")
