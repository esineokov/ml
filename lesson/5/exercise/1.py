print("Enter line-by-line data to write to the file. At the end, send an empty string.")
with open("file.txt", "w") as file:
    while True:
        data = input()
        if data:
            file.write(data + "\n")
        else:
            break

